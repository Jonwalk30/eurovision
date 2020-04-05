import pandas as pd
from judge import Judge
import numpy as np
import mp3
import conf
import time


def read_countries(countries: []):
    for country in countries:
            read(country)


def read(judge: Judge):
    read_greeting(judge)
    dp_c = read_votes(judge)
    read_douze_points(judge, dp_c)


def read_greeting(judge: Judge):
    input("Press Enter to hear from " + judge.name + "...")
    set_active_judge(judge.name)
    mp3.play(conf.mp3_fp + judge.name + "_greeting.mp3")


def read_votes(judge: Judge):
    input("Press Enter to see who " + judge.name + " voted for...")
    mp3.play(conf.mp3_fp + judge.name + "_we_have_voted.mp3")
    print(judge.name, "has assigned points as follows... ")
    print()
    regular_votes = []
    for c, v in judge.votes:
        if not (v == 12):
            print(c.ljust(15) + " : " + str(v))
            regular_votes = regular_votes + [(c, v)]
        else:
            dp_c = c
    print()
    update_table(regular_votes)
    return dp_c


def read_douze_points(judge: Judge, dp_c :str):
    input("Press Enter to see who received douze points...!")
    print()
    mp3.play(conf.mp3_fp + judge.name + "_douze_points.mp3")
    print("And le douze points go to...")
    print()
    time.sleep(3)
    print(dp_c)
    mp3.play(conf.mp3_fp + dp_c + "_from_" + judge.name + "_name.mp3")
    print()
    print()
    update_table([(dp_c, 12)])


def set_active_judge(judge_name: str):
    table = pd.read_csv(conf.league_table_fp, index_col = "Country")
    table["Points_Gained"] = 0
    table["Active_Judge"] = [1 if country  == judge_name else 0 \
        for country in table.index]
    table.to_csv(conf.league_table_fp)


def update_table(votes: []):
    table = pd.read_csv(conf.league_table_fp, index_col = "Country")
    for c, v in votes:
        table.loc[c].at['Points'] = table.loc[c]['Points'] + v
        table.loc[c].at['Points_Gained'] = v
    table.to_csv(conf.league_table_fp)


def final_update_table(players: [], points_multiplier: int):
    table = pd.read_csv(conf.league_table_fp, index_col = "Country")
    table = table.reset_index()
    table["Points_Gained"] = 0
    table["Active_Judge"] = 0
    table_sorted = table.sort_values(by=["Points","Country"], \
        ascending=[True, False])
    for c in table_sorted["Country"]:

        table_sorted["Active_Judge"] = np.where(table_sorted["Country"] == c, \
            1, table_sorted["Active_Judge"])
        table_sorted = table_sorted.set_index("Country")
        table_sorted.to_csv(conf.league_table_fp)
        table_sorted = table_sorted.reset_index()
        input("Press Enter To See Final Score: ")
        table_sorted["Points_Gained"] = np.where(table_sorted["Country"] == c, \
            sum_points(c, players, points_multiplier), \
            table_sorted["Points_Gained"])
        table_sorted["Points"] = np.where(table_sorted["Country"] == c, \
        table_sorted["Points"] + table_sorted["Points_Gained"], \
        table_sorted["Points"])
        table_sorted = table_sorted.set_index("Country")
        table_sorted.to_csv(conf.league_table_fp)
        table_sorted = table_sorted.reset_index()
        input("Press For Next Country")
        table_sorted["Active_Judge"] = np.where(table_sorted["Country"] == c, \
            2, table_sorted["Active_Judge"])

    table["Active_Judge"] = 0


def sum_points(country: str, players: [], points_multiplier: int):
    points = 0
    for player in players:
        for c, v in player.votes:
            if c == country:
                points = points + (v * points_multiplier)
    return points
