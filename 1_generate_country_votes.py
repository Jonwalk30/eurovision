import pandas as pd
import random as r
import args
import judge as j
import conf

seed = args.grab_seed_as_arg()
r.seed(seed)

country_names = pd.read_csv(conf.countries_fp)["Country"].tolist()
possible_scores = pd.read_csv(conf.possible_scores_fp)["Score"].tolist()

countries = j.create_judge_list(country_names, r)
countries = j.generate_judge_scores(countries, possible_scores, r)

# j.print_judges(countries)
j.save_judges_as_json(countries, conf.jury_votes_fp)
