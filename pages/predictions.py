import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import xgboost
from app import app
from joblib import load
import pandas as pd

pipeline = load('assets/pipeline.joblib')
print('Pipeline loaded!')

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
        dcc.Markdown('## Break Points Faced', className='mb-5'), 
        dcc.Markdown('#### Player A'),
        dcc.Slider(
            min=0,
            max=20,
            step=1,
            value=3,
        ),  
        dcc.Markdown('## Break Points Faced', className='mb-5'), 
        dcc.Markdown('#### Player B'),
        dcc.Slider(
            min=0,
            max=20,
            step=1,
            value=3,
        ),
        dcc.Markdown('## Break Points Saved', className='mb-5'), 
        dcc.Markdown('#### Player A'),
        dcc.Slider(
            min=0,
            max=20,
            step=1,
            value=3,
        ),  
        dcc.Markdown('## Break Points Saved', className='mb-5'), 
        dcc.Markdown('#### Player B'),
        dcc.Slider(
            min=0,
            max=20,
            step=1,
            value=3,
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

@app.callback(
    Output('prediction-content', 'value'),
    [
    Input('Player_A', 'value'), 
    Input('Player_B', 'value'),
    Input('Player_A_bpFaced', 'value'),
    Input('Player_B_bpFaced', 'value'),
    Input('Player_A_bpSaved', 'value'),
    Input('Player_B_bpSaved', 'value')],
)
def predict(Player_A, Player_B, Player_A_bpFaced, Player_B_bpFaced, Player_A_bpSaved, Player_B_bpSaved):
    df = pd.DataFrame(
        columns = ['Player_A', 'Player_B', 'Player_A_bpFaced', 
             'Player_B_bpFaced','Player_A_bpSaved', 'Player_B_bpSaved'],
        data=[[Player_A, Player_B, Player_A_bpFaced, Player_B_bpFaced, Player_A_bpSaved, Player_B_bpSaved]]
    )
    y_pred = pipeline.predict(df)[0]
    return y_pred