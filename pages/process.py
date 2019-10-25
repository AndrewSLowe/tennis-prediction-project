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

row4 = dbc.Row(
    [
        dcc.Markdown(
            """
            #### Results
            ##### My baseline (i.e. the prediction one would make without measuring the influence of different features) would be a 50/50. It's a coing flip when you ignore who the players are, their win/loss ratios, their highest ranks, possible match-specific circumstances like breakpoints faced and saved, etc., and just account for the fact that they are two players playing a game where only one player can win. That's a prediction a third grader could make with a little guidance.
            ##### But once I built a machine learning model my accuracy score went up to 78% test accuracy. The idea is that, given the 50+ features in my machine learning model, that it would predict the winner of a tennis match 78% of the time.
            ##### These are good results, but I wanted to make my model with features that a user would care about. So I stripped away a lot of the noise (features that had little positive effect on the accuracy score), and obly kept the names of the two players, how many break points they faced, and how many break points they saved. For non-tennis players, a break point is a pivotal moment in a match. So for those who aren't interested in the scoring a rules of tennis but want to use my app anyways, just know what facing a break point is bad for a player, and saving a break point is good for a player. Shaving the rest of these features only brought my accuracy score down by 2 points, to 76%. Still a very strong model that users can now interacy with.
            """
        )
    ]
)
row5 = dbc.Row(
    [
        dcc.Markdown(
            """
            #### Feature Analysis
            ##### Below we see what is called a partial dependency plot of the variable that had the highest impact on my model's accuracy score, "Player_A_bpFaced". This is how many break points player A faced (again, break points are bad for the player who's facing them). 
            ##### This partial dependency plot is like a more complex picture of what the chart above on permutation importances tells us about this one feature. The chart above tells us that this feature has the most influence on the model of any feature, but we don't know from that in which direction it takes our predictions or the extent at different amount of break points faced. So looking at this graph, we see that break points faced by player A is monotonic (one directional). Furthermore, a the amount of break points that Player A faced increases, odds start to look worse and worse for her chance of winning the match. The influence of Player B break points faced goes in the opposite directions and tells us the same thing for Player B's odds of winning. 
            """
        )
    ]
)
row6 = dbc.Row(
    [
        html.Img(src='assets/PDP.png',
                         className='img-fluid',
                         style={'display': 'block',
                                'margin-left': 'auto',
                                'margin-right': 'auto',
                                'margin-top':'2%',
                                'width' : '90%'}
                        ),
    ]
)
row7 = dbc.Row(
    [
        dcc.Markdown(
            """
            ##### Below is the same kind of graph but for the opposite variable, for break points faced by Player B. This has the opposite effect: as the amount of break points faced by player B increases, so does the chance of Player A winning. Notice, though, that this graph has more lines than the above PDP. The fainter lines represent the effect of Break points faced by Player B for each individual observation, while the bold line is its effect on average.
            """
        )
    ]
)


row8 = dbc.Row(
    [
        html.Img(src='assets/PDP2.png',
                         className='img-fluid',
                         style={'display': 'block',
                                'margin-left': 'auto',
                                'margin-right': 'auto',
                                'margin-top':'2%',
                                'width' : '90%'}
                        ),
    ]
)

row9 = dbc.Row(
    [
        dcc.Markdown(
            """
            ##### It might also be helpful to see the interaction between these contrasting features. Below we see a 2 feature partial dependency plot with Player A break points saved and Player A break points Faced. As we can see, as the number of break points goes up, the number in the boxes goes up. As that number increases, the prediction that player A will win the match goes down, and so we can see that Player A break points saved and faced has an inverse relationship, because their chance of winning goes up as the amount of break points saved they have goes up, but goes down as the amount of break points they face goes up,
            """
        )
    ]
)


row10 = dbc.Row(
    [
        html.Img(src='assets/PDP2Feats.png',
                         className='img-fluid',
                         style={'display': 'block',
                                'margin-left': 'auto',
                                'margin-right': 'auto',
                                'margin-top':'2%',
                                'width' : '90%'}
                        ),
    ]
)

row11 = dbc.Row(
    [
        dcc.Markdown(
            """
            ##### Finally, lets look at the effect of each feature on a specific match in relation to one another. This shap graph shows the interaction between all of these features in the match. The middle, at value 0, represents our 50/50 baseline, a coin flip as to who we would predict to win the match. But given the Player names, the amount of break points they faced and saved, it predicts rather that 
            """
        )
    ]
)


row12 = dbc.Row(
    [
        html.Img(src='assets/shap.png',
                         className='img-fluid',
                         style={'display': 'block',
                                'margin-left': 'auto',
                                'margin-right': 'auto',
                                'margin-top':'2%',
                                'width' : '90%'}
                        ),
    ]
)

layout = dbc.Row([row1, row2, row3, row5, row6, row7, row8, row9, row10, row11, row12])