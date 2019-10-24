import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

row1 = dbc.Row(
    [
        dcc.Markdown(
            """
        
            ## About the Model
            """,
            className= 'mb-3'
        ),
        dcc.Markdown(
            """
            #### **Project Inspiration**
            ##### My inspiration for the tennis match outcome predictor was actually from a Lambda student from an earlier Cohort, Scott Huston, who made an NFL team run/pass predictor called "Robo Romo." I thought that if Scott could make a model that would predict whether a team would run or pass, I should be able to predict who would win in a tennis match between two players, given some relevant information about the match and who the players were. Being a tennis fan, I was excited for the challenge.
            """,
            className= 'mb-3'

        )
    ],
)
row2 = dbc.Row(
    [
        dcc.Markdown(
            """
            #### ** Process **
            """
        )
    ],
    className = 'mt-5'
)
col1 = dbc.Col(
    [  
        html.Img(src='assets/Permutation_Importances.png',
                         className='img-fluid',
                         style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '90%'}
                        ),
    ],
    md = 3
)

col2 = dbc.Col(
    [
        dcc.Markdown(
            """
            ##### I began by finding a dataset from github.com/JeffSackman who has information from every professional tennis match over the past 50 years. After many hours of combining these dataframes, I was finally ready to do some analysis. 
            ##### Machine learning models have features (different variables used to predict the target variable; in my case, the target is which player won a match). But half of the variables I didn't even understand, (P.S. If anyone can tell me what "1stWon means", please email me ASAP.) so my goal was to reduce the complexity of my model by getting rid of features that weren't positively influencing my model and that wouldn't be interesting features for a user to use to predict a match. On the right we can see a list of my top feature importances--those that most positively influenced my model's accuracy (a metric that doesn't need to be understood quite yet).
            ##### I decided just to stick with the player names, how many break points they faced and how many break points they saved.
            """,
        )
    ],       
)
row3 = dbc.Row([col1,col2])



layout = dbc.Row([row1, row2, row3])