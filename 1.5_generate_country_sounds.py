import pandas as pd
import mp3
import judge as j
import conf


df = pd.read_csv(conf.countries_fp)
df["Language"] = df["Language"].fillna("en-us")
df["Greeting"] = df["Greeting"].fillna("Hello, house party!")

countries = j.load_judges_from_json(conf.jury_votes_fp)

for _, row in df.iterrows():

    name = row["Country"]
    language = row["Language"]

    text = row["Greeting"] + " " + row["Country"] +  \
        " calling! We are live from " + row["Capital"]
    mp3.save(conf.mp3_fp + name + "_greeting.mp3", text, language)

    text = "We have voted as follows"
    mp3.save(conf.mp3_fp + name + "_we_have_voted.mp3", text, language)

    text = "Et le douze points go to"
    mp3.save(conf.mp3_fp + name + "_douze_points.mp3", text, language)

    for country in countries:
        if country.name == row["Country"]:
            for c, v in country.votes:
                if v == 12:
                    text = c
                    name = c + "_from_" + country.name

    mp3.save(conf.mp3_fp + name + "_name.mp3", text, language)
