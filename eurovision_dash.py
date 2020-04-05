import dash
import dash_html_components as html
import numpy as np
from dash.dependencies import Input, Output, State
from dash_table import DataTable
import dash_core_components as dcc

import pandas as pd

columns = [
    {"id": 0, "name": "Direction"},
    {"id": 1, "name": "Position"},
    {"id": 2, "name": "Country"},
    {"id": 3, "name": "Points"},
    {"id": 4, "name": "Point_Gained_Str"}
]

def get_data():

    filepath = "/Users/Jonathanwalker/Desktop/new/drinking_games/data/"
    table_fp = filepath + 'league_table.csv'

    df = pd.read_csv(table_fp)

    df['Country'] = df['Country'].str.upper()
    df['Point_Gained_Str'] = ["(+" + str(p) + ")" if p > 0 else "     " for p in df["Points_Gained"]]
    df['Points_Before'] = df["Points"] - df["Points_Gained"]

    df = df.sort_values(by=["Points_Before","Country"], ascending=[False, True])
    df['Position_Before'] = np.arange(len(df)) + 1

    df = df.sort_values(by=["Points","Country"], ascending=[False, True])
    df['Position'] = np.arange(len(df)) + 1

    df['Direction'] = np.where(df['Position'] < df["Position_Before"], '⬆',
                        np.where(df['Position'] == df["Position_Before"], '', '⬇'))

    df = df[["Direction", "Position", "Country", "Points", "Point_Gained_Str", "Active_Judge"]]

    return df

def get_table(table_id: str):
    return DataTable(
        id=table_id,
        data=[],
        style_table={
        'margin':'0 auto'
        },
        style_as_list_view=True,
        style_data_conditional=[
            {
                'if': {
                    'filter_query': '{5} eq 1'
                },
                'backgroundColor': 'yellow',
                'color': 'black',
            },
        ] + [
            {
                'if': {
                    'filter_query': '{5} eq 2'
                },
                'backgroundColor': 'white',
                'color': 'navy',
            },
        ] + [
            {
                'if': {
                    'column_id': 0,
                    'filter_query': '{0} eq ⬆'
                },
                'color': '#39FF14',
            },
        ] + [
            {
                'if': {
                    'column_id': 0,
                    'filter_query': '{0} eq ⬇'
                },
                'color': '#FF2400',
            },
        ],
        style_cell_conditional=[
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in [2,4]
        ] + [
            {
                'if': {'column_id': c},
                'textAlign': 'center'
            } for c in [1,3]
        ],
        style_data={
            'border': '4px solid rgb(15, 56, 114, .0)'
        },
        style_cell=
        {
            'backgroundColor': 'rgb(10, 113, 204)',
            'color': 'white',
            'font-family': 'Arial',
            'font-weight': 'bold'
        }
        ,
        style_header={'display': 'none'}
    )

df = get_data()

app = dash.Dash(__name__)

app.layout = html.Div(
    [html.Div(children=[
        html.Div(children=[
            get_table('table1')
        ], className="three columns"),
        html.Div(children=[
            get_table('table2')
        ], className="three columns"),
        html.Div(children=[
            get_table('table3')
        ], className="three columns")
    ],
    className="row"),
    dcc.Interval(id='table-update',interval=1000)],
    style={
        'padding-top': 240,
        'padding-left': 90
    }, className="offset-by-one column ")

@app.callback(
    [Output("table1", "data"), Output('table1', 'columns')],
    [Input('table-update', 'n_intervals')]
)
def updateTable1(a):
    df = get_data()
    return df.values[0:14], columns

@app.callback(
    [Output("table2", "data"), Output('table2', 'columns')],
    [Input('table-update', 'n_intervals')]
)
def updateTable2(a):
    df = get_data()
    return df.values[14:28], columns

@app.callback(
    [Output("table3", "data"), Output('table3', 'columns')],
    [Input('table-update', 'n_intervals')]
)
def updateTable3(a):
    df = get_data()
    return df.values[28:41], columns


if __name__ == "__main__":
    app.run_server(port=8054)
