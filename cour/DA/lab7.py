import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.static import teams
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import leaguegamefinder
import requests

dict_={'a':[11,21,31],'b':[12,22,32]}
df=pd.DataFrame(dict_)
print(type(df))

print(df.head())

print(df.mean())

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

nba_teams = teams.get_teams()
print(nba_teams[0:3])

dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
print(df_teams.head())

df_warriors=df_teams[df_teams['nickname']=='Warriors']
print(df_warriors)

id_warriors=df_warriors[['id']].values[0][0]
# we now have an integer that can be used to request the Warriors information 
print(id_warriors)

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
gamefinder.get_json()
games = gamefinder.get_data_frames()[0]
print(games.head())

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"
def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

download(filename, "Golden_State.pkl")

file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
print(games.head())

games_home=games[games['MATCHUP']=='GSW vs. TOR']
games_away=games[games['MATCHUP']=='GSW @ TOR']

print(games_home['PLUS_MINUS'].mean())

print(games_away['PLUS_MINUS'].mean())

fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
#print(plt.show())

#Calculate the mean for the column PTS 
#for the dataframes games_home and  games_away
print(games_home['PTS'].mean())
print(games_away['PTS'].mean())
