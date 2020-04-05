import judge as j
import conf
import manage_table as mt

players = j.load_judges_from_json(conf.player_votes_fp)

mt.final_update_table(players, 5)
