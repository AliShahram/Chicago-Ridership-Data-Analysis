import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

from loader import *


db = DatabaseConnection()
df = db.get_table_data()
labels, values = db.get_express_route()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div(children=[

    html.H1(children='CTA Ridership'),
    html.H4(children='Data Visualization and Analysis'),

    html.Div([
        dash_table.DataTable(
            id='datatable-interactivity',
            columns=[
                {"name": i, "id": i, "deletable": True} for i in df.columns
            ],
            data=df.to_dict('records'),
            editable=True,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            row_selectable="multi",
            row_deletable=True,
            selected_rows=[],
            page_action="native",
            page_current= 0,
            page_size= 10,
        )
    ], style={'width':'100%', 'marginLeft' : '20px'}
    ),

    #Pie Chart
    html.Div([
        dcc.Graph(id='device_usage',
                figure=go.Figure(
                    data=[go.Pie(labels=labels,
                                    values=values)],
                    layout=go.Layout(
                        title='Route Efficiency by boardings and alightings')
            ))
    ], style = {'marginRight':'470px'}),

    html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id = 'xaxis-column',
                    options=[
                        {'label': 'Bus Stop', 'value': 'stop_id'},
                        {'label': 'Routes', 'value': 'routes'}
                    ],
                    value='routes',
                    style={'width':'200px',
                    'height':'40px'
                    },
                )
            ],
            style={'marginTop': '100px'}),

            html.Div([
                dcc.Dropdown(
                    id = 'yaxis-column',
                    options=[
                        {'label': 'Bus Stop', 'value': 'stop_id'},
                        {'label': 'Boardings', 'value': 'boardings'},
                        {'label': 'Routes', 'value': 'routes'},
                        {'label': 'alightings', 'value': 'alightings'}
                    ],
                    value='boardings',
                    style={'width':'200px',
                    'height':'40px'
                    },
                )
            ],
            style={'marginTop': '10px'}),
        ],
        style = {'width': '30%', 'float': 'right', 'bordor': 'solid, 1px'}),


        html.Div([
            dcc.Graph(id='individuals-graph')
        ],
        style = {'width' : '70%', 'float' : 'left'})
    ],
    style = {'width' : '100%', 'heightMin' : '500px'}),



#Aggregate Graph
    html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id = 'xaxis-column-agg',
                    options=[
                        {'label': 'Bus Stop', 'value': 'stop_id'},
                        {'label': 'Routes', 'value': 'routes'}
                    ],
                    value='routes',
                    style={'width':'200px',
                    'height':'40px'
                    },
                )
            ],
            style={'marginTop': '420px'}),

            html.Div([
                dcc.Dropdown(
                    id = 'yaxis-column-agg',
                    options=[
                        {'label': 'Bus Stop', 'value': 'stop_id'},
                        {'label': 'Boardings', 'value': 'boardings'},
                        {'label': 'Routes', 'value': 'routes'},
                        {'label': 'alightings', 'value': 'alightings'}
                    ],
                    value='boardings',
                    style={'width':'200px',
                    'height':'40px'
                    },
                )
            ],
            style={'marginTop': '10px'}),
        ],
        style = {'width': '30%', 'float': 'right'}),

        html.Div([
            dcc.Graph(id='aggregates-graph')
        ],
        style = {'width' : '70%', 'float' : 'left'})
    ],
    style = {'width': '100%', 'heightMin' : '500px'}),

])

@app.callback(
    Output('individuals-graph', 'figure'),
    [Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value')])
def update_ind_graph(xaxis_column_name, yaxis_column_name):
    x_values, y_values = db.get_graph_data(xaxis_column_name, yaxis_column_name)

    return {
        'data': [
            {
                'x' : x_values,
                'y' : y_values,
                'mode': 'markers',
                'marker': {'size': 4}
            }
        ],
        'layout' : {
            'title' : 'Individual Data',
            'xaxis' : {
                'title': xaxis_column_name
            },
            'yaxis' : {
                'title': yaxis_column_name
            }
        }
    }




@app.callback(
    Output('aggregates-graph', 'figure'),
    [Input('xaxis-column-agg', 'value'),
    Input('yaxis-column-agg', 'value')])
def update_agg_graph(xaxis_column_agg_name, yaxis_column_agg_name):
    x_values, y_values = db.get_agg_data(xaxis_column_agg_name, yaxis_column_agg_name)

    return {
        'data': [
            {
                'x' : x_values,
                'y' : y_values,
                'type': 'bar'
            }
        ],
        'layout' : {
            'title' : 'Aggregate Data',
            'xaxis' : {
                'title': xaxis_column_agg_name
            },
            'yaxis' : {
                'title': yaxis_column_agg_name
            },
        }
    }




if __name__ == '__main__':
    app.run_server(debug=True)
