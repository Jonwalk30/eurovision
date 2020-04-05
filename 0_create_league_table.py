import pandas as pd
import conf

league_table = pd.read_csv(conf.countries_fp)

league_table["Position"] = league_table.index + 1
league_table["Points"] = 0
league_table["Points_Gained"] = 0
league_table["Active_Judge"] = 0

league_table[["Country", "Points", "Points_Gained", "Active_Judge"]]\
    .set_index("Country").to_csv(conf.league_table_fp)
