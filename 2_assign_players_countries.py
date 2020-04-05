import pandas as pd
import random as r
import player as p
import conf
import args

seed = args.grab_seed_as_arg()
r.seed(seed)

countries = pd.read_csv(conf.countries_fp)["Country"].tolist()
player_names = pd.read_csv(conf.players_fp)["Player"].tolist()

players = p.create_player_list(player_names, r)
players = p.assign_countries_to_players(players, countries, r)
p.print_players_countries(players)
