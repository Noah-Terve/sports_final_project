#imports 
import requests, time
from datetime import datetime
from bs4 import BeautifulSoup

import csv
import pprint

# Getting Player Collages Data
path = "nba_draft_info.html"
with open(path) as file:
    soup = BeautifulSoup(file, "html.parser")


table = soup.find(class_ = "Crom_table__p1iZz")
rows = table.find_all('tr')

college_info = {} # {player: school_name}

for i in range(1, len(rows)):
    col = rows[i].find_all('td')
    if col:
        try:
            name = col[0].find('a').string
            college = col[2].string
            college_info[name] = college
        except:
            name = col[0].find('span').string
            college = col[2].string
            college_info[name] = college


draft_names = college_info.keys() # All names of players in the nba draft info
per_names = []

with open ("Player Per Game.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        per_names.append(row[3])

per_names = list(set(per_names)) # Set of names who are in the player per game

# remove names that aren't in the player per game dataset
names_to_pop = []
for name in draft_names:
    if not name in per_names:
        names_to_pop.append(name)

for name in names_to_pop:
    college_info.pop(name)

# iterate over the players we have left, build school to player mapping
schools = {} # schools -> {school : [Player -> [season stat list], Player -> [season stat list]]}
draft_names = college_info.keys()
for name in draft_names:
    try:
        schools[college_info[name]][name] = []
    except:
        schools[college_info[name]] = {name : []}

schools.pop(None)

# remove schools with less than 5 people in them
schools_to_remove = []
for school in schools:
    if len(school) < 5:
        schools_to_remove.append(school)

for school in schools_to_remove:
    schools.pop(school)


YEAR = 1
PTS = 34
REBOUNDS = 28
ASSISTS = 29
STEALS = 30
BLOCKS = 31
FG_ATTEMPTS = 14
MADE_FG = 13
FREE_THROW_ATTEMPTS = 24
FREE_THROWS_MADE = 23
TURN_OVERS = 32
with open ("Player Per Game.csv") as file:
    reader = csv.reader(file)
    i = 0
    for row in reader:
        if i == 0:
            keys = row
            i += 1
            continue
        # name -> row[3]
        # lookup school based on name
        # in schools find player
        # build dictionary from row 
        # add dicitonary to their list of stats
        try:
            school_name = college_info[row[3]]
            schools[school_name][row[3]].append(
                (int(row[YEAR]), float(row[PTS]), float(row[REBOUNDS]), float(row[ASSISTS]), float(row[STEALS]),
                 float(row[BLOCKS]), float(row[FG_ATTEMPTS]), float(row[MADE_FG]), 
                 float(row[FREE_THROW_ATTEMPTS]), float(row[FREE_THROWS_MADE]), float(row[TURN_OVERS])))
        except Exception as e:
            # player is not in the players that we have school info on
            pass

# post processing, only take the first 4 seasons of data
for school in schools:
    for player in schools[school]:
        player_val = schools[school][player]
        # remove anything from the last 4 years (2020 - 2024)
        # remove any duplicates
        # remove anything beyond their 4 oldest seasons
        last_year = 0
        idxs_to_pop = []
        for i in range(len(player_val)):
            year, *_ = player_val[i]
            # if year >= 2020:
            #     idxs_to_pop.append(i)

            if year == last_year:
                idxs_to_pop.append(i)
        
            last_year = year

        for idx in idxs_to_pop[::-1]:
            player_val.pop(idx)
        
        # only get their first 4 seasons
        if (len(player_val) < 4):
            school[school].pop(player)
        else:
            schools[school][player] = player_val[-4:]
        

# go through schools, calculate values for each player

# calculate spread for each school

pprint.pp(schools)