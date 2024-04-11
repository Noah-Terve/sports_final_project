#imports 
import requests, time
from datetime import datetime
from bs4 import BeautifulSoup

import csv

# Steps taken to get the actual html to scrape:
# go to this site: https://www.nba.com/stats/draft/history
# select 'All' under page, then download the html.
# Pretify that (for readability), I used https://webformatter.com/html
# Copy over to this directory so we can read from it

# Table class = "Crom_table__p1iZz"

path = "nba_draft_info.html"
with open(path) as file:
    soup = BeautifulSoup(file, "html.parser")


table = soup.find(class_ = "Crom_table__p1iZz")
rows = table.find_all('tr')

college_info = {}

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

print(college_info)