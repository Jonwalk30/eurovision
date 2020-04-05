import pandas as pd
import judge as j
import conf

country_names = pd.read_csv(conf.countries_fp)["Country"].tolist()

players = j.input_judges_scores(country_names)
j.save_judges_as_json(players, conf.player_votes_fp)
