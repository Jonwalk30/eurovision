import judge as j
import conf
import manage_table as mt

countries = j.load_judges_from_json(conf.jury_votes_fp)

mt.read_countries(countries)
