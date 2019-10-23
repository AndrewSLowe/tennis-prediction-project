import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import xgboost
from app import app
from joblib import load

pipeline = load('assets/pipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown('## Match up', className='MB-5'),
        dcc.Markdown('#### Player A'), 
        dcc.Input(
            placeholder="Enter a player's name...",
            type='text',
            value='',
        ),
        dcc.Markdown('#### Player B', className='mb-5'), 
        dcc.Input(
            placeholder="Enter a player's name...",
            type='text',
            value=''
        ), 
    ],
    md=4,
)
     
column2 = dbc.Col(
    [
        html.H2('Expected Winner', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2])