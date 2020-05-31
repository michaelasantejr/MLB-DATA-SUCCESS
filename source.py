import pandas as pd

#exec(open("source.py").read())
mlb = pd.read_csv('mlb_elo.csv')
teams = sorted(list(mlb[mlb.season == 2019].team1.unique()))

home_games = mlb.groupby('team1').team1.count().filter(items =teams)
away_games = mlb.groupby('team2').team2.count().filter(items =teams)
################################# Run Dif####################################
def calc_rundiff():
    home_scores  = mlb.groupby('team1').score1.sum().filter(items = teams)
    away_scores = mlb.groupby('team2').score2.sum().filter(items = teams)
    #runs = pd.DataFrame({'total_score': home_scores + away_scores})
    home_scores_allowed  = mlb.groupby('team1').score2.sum().filter(items = teams)
    away_scores_allowed = mlb.groupby('team2').score1.sum().filter(items = teams)
    return((home_scores_allowed + away_scores_allowed)/(home_games + away_games))
    
    ######################################Probabilities ###################################

def calc_prob(): #This calculates the average prob of each team
    home_psum = mlb.groupby('team1').elo_prob1.sum().filter(items = teams)
    away_psum = mlb.groupby('team2').elo_prob2.sum().filter(items = teams)
    return((home_psum + away_psum)/(home_games + away_games))

    ######################################### Playoffs ##################################################
def calc_playoff():
    mlb = pd.read_csv('mlb_elo.csv')
    mlb_playoff = mlb[mlb.playoff.notna()]

    home_playoff_wins_by_season = mlb_playoff[mlb_playoff.score1 > mlb_playoff.score2].groupby(['season','team1','team2'],as_index = False).team1.size().reset_index()
    away_playoff_wins_by_season = mlb_playoff[mlb_playoff.score2 > mlb_playoff.score1].groupby(['season','team2','team1'],as_index = False).team2.size().reset_index()
    playoff_wins_by_season = pd.concat([home_playoff_wins_by_season, away_playoff_wins_by_season]).groupby(['season','team1','team2'])[0].sum().reset_index()
    playoff_wins_by_season['teams'] = playoff_wins_by_season[['team1','team2']].apply(lambda x: ''.join(sorted(x)),axis = 1)
    playoff_wins_by_season.groupby(['season','teams']).apply(lambda x: x.loc[x[0]==x[0].max(),['season','team1']]) 
   # print(playoff_wins_by_season)
    winner= playoff_wins_by_season.groupby('team1').team1.size()
    return winner

    ##################### World Series ###########################
def calc_worldseries(): 
    mlb = pd.read_csv('mlb_elo.csv')
    mlb_series = mlb[mlb.playoff.notna()]
    
    
    home_series_wins_by_season = mlb_series[mlb_series.score1 > mlb_series.score2].groupby(['season','team1','team2'],as_index = False).team1.size().reset_index()
    away_series_wins_by_season = mlb_series[mlb_series.score2 > mlb_series.score1].groupby(['season','team2','team1'],as_index = False).team2.size().reset_index()
    series_wins_by_season = pd.concat([home_series_wins_by_season, away_series_wins_by_season]).groupby(['season','team1','team2'])[0].sum().reset_index()
    series_wins_by_season['teams'] = series_wins_by_season[['team1','team2']].apply(lambda x: ''.join(sorted(x)),axis = 1)
    series_wins_by_season.groupby(['season','teams']).apply(lambda x: x.loc[x[0]==x[0].max(),['season','team1']])
    #print(wins.head())
    for team in teams:
        if team not in series_wins_by_season.index:
            series_wins_by_season = series_wins_by_season.append(pd.Series({team: 0}),ignore_index = True)
    #series_wins_by_season.to_csv(r'wins.csv')
    wins = series_wins_by_season.groupby('team1').team1.size()
    return wins
######################## CALCULATE index MY DATAFRAME ###############################################
def everything():
    dicti = {'team':teams,
            'games_played': home_games + away_games, 
            'total_prob_avg' : calc_prob(),
            'total_diff': calc_rundiff(),
            'plf_wins': calc_playoff()}
    df = pd.DataFrame(dicti).set_index('team')
    return df   
def everything_with_ranks(a_df):
    dicti = {'team':teams,
            'games_played': home_games + away_games, 
            'total_prob_avg' : calc_prob(),
            'total_diff': calc_rundiff(),
            'plf_wins': calc_playoff(),
            #'total_ranking': calc_rank(a_df).rank(ascending = 1),
            'raw_rank': calc_rank(a_df) }
    df = pd.DataFrame(dicti).set_index('team')
    return df   
    ######################################## Rank ###############################################
def calc_rank(total_df):
    for column in total_df.columns:
        rank_column = column + '_rank'
        total_df[rank_column] = (total_df[column].max() - total_df[column])/(total_df[column].max() - total_df[column].min())* (len(teams)-1) + 1
    rank_columns = total_df.columns[total_df.columns.str.contains('_rank')== True]
    my_rank = total_df[rank_columns]
    ranks = my_rank.sum(axis = 1)
    return(ranks)
######################### MAIN FUNCTION IN PROGRAM #######################################################
my_df = everything()
#displays what we need
dictin = {'team': teams,
          'weighted_rank': calc_rank(my_df)}
my_df = pd.DataFrame(dictin).set_index('team')
my_df.sort_values(by =['weighted_rank'],inplace = True,ascending = True)
print(my_df)

