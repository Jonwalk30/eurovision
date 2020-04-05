import random
import json

import mp3

class Judge:

    name = None
    votes = []

    def __init__(self, name):
        self.name = name


def create_judge_list(judge_names: [], r):
    judge_names_shuffled = judge_names.copy()
    r.shuffle(judge_names_shuffled)
    judges = []
    for judge_name in judge_names_shuffled:
        new_judge = Judge(name= judge_name)
        judges = judges + [new_judge]
    return judges


def generate_judge_scores(countries: [], possible_scores: [], r):
    countries_post_vote = countries.copy()
    for country in countries_post_vote:
        countries_voted_for = r.sample(\
            [c for c in countries if c != country], len(possible_scores))
        scores_given = possible_scores.copy()
        for c, v in zip(countries_voted_for, scores_given):
            country.votes = country.votes + [(c.name, v)]
    return countries_post_vote


def load_judges_from_json(from_pth: str):
    with open(from_pth) as json_file:
        data = json.load(json_file)
    judges = []
    for d in data:
        j = Judge(d["name"])
        j.votes = d["votes"]
        judges = judges + [j]
    return judges


def save_judges_as_json(judges: [], to_pth: str):
    with open(to_pth, "w") as file:
        json.dump([judge.__dict__ for judge in judges], file)


def print_judges(judges: []):
    for judge in judges:
        print(judge.name, "has assigned points as follows... ")
        print()
        for c, v in judge.votes:
            if not (v == 12):
                print(c.ljust(15) + " : " + str(v))
            else:
                dp_c = c
        print()
        print("And le douze points go to...")
        print()
        print(dp_c)
        print()
        print()


def input_judges_scores(countries: []):
    players = []
    keep_listening = True
    while(keep_listening):
        players = players + [input_judge_scores(countries)]
        more_players_check = input("Add another player's votes?")
        if ("Y" not in more_players_check.upper()):
            keep_listening = False
    return players


def input_judge_scores(countries: []):
    name = input("Player name:")
    player = Judge(name)
    v = read_in_country(player.name + " awards 1 point to...", countries)
    player.votes = player.votes + [(v, 1)]
    for i in (2,3,4,5,6,7,8,10):
        v = read_in_country(player.name + " awards " + str(i) + " points to...", countries)
        player.votes = player.votes + [(v, i)]
    v = read_in_country(player.name + " awards douze points to...", countries)
    player.votes = player.votes + [(v, 12)]
    return player


def read_in_country(print_text: str, countries: []):
    no_valid_input = True
    while(no_valid_input):
        c = input(print_text)
        if c in countries:
            no_valid_input = False
        else:
            print("Invalid Country, please try again.")
    return c


def read(judge: Judge, mp3_fp: str, table_fp: str):

    input("Press Enter to hear from " + judge.name + "...")
    set_active_judge(table_fp, judge.name)
    play(mp3_fp + judge.name + "_greeting.mp3")

    input("Press Enter to see who " + judge.name + " voted for...")
    play(mp3_fp + judge.name + "_we_have_voted.mp3")

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

    update_table(table_fp, regular_votes)

    input("Press Enter to see who received douze points...!")
    print()
    play(mp3_fp + judge.name + "_douze_points.mp3")


    print("And le douze points go to...")
    print()

    time.sleep(5)

    print(dp_c)
    play(mp3_fp + dp_c + "_from_" + judge.name + "_name.mp3")
    print()
    print()

    update_table(table_fp, [(dp_c, 12)])

def read_countries(countries: [], mp3_fp: str, table_fp: str):
    for country in countries:
            read(country, mp3_fp, table_fp)
