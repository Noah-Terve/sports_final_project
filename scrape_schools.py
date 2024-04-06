#imports 
import requests, time
from datetime import datetime
from bs4 import BeautifulSoup

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

for i in range(1, len(rows)):
    col = rows[i].find_all('td')
    if col:
        try:
            print(f"Name: {col[0].find('a').string}, College: {col[2].string}")
        except:
            print(f"Name: {col[0].find('span').string}, College: {col[2].string}")
        

# short excerpt for sorting
# <table class="Crom_table__p1iZz">
#     <thead>
#         <tr class="Crom_headers__mzI_m">
#             <th sort="true" class="Crom_text__NpR1_ Crom_primary__EajZu Crom_sticky__uYvkp" field="PLAYER_NAME">
#                 <br />
#                 Player
#             </th>
#             <th sort="true" field="TEAM_ABBREVIATION" class="Crom_text__NpR1_ Crom_primary__EajZu">Team</th>
#             <th sort="true" dir="D" field="ORGANIZATION" class="Crom_text__NpR1_ Crom_primary__EajZu">Affiliation</th>
#             <th sort="true" dir="D" field="SEASON">Year</th>
#             <th sort="true" dir="D" field="ROUND_NUMBER">
#                 Round<br />
#                 Number
#             </th>
#             <th sort="true" dir="D" field="ROUND_PICK">
#                 Round<br />
#                 Pick
#             </th>
#             <th sort="true" dir="D" field="OVERALL_PICK">
#                 Overall<br />
#                 Pick
#             </th>
#         </tr>
#     </thead>
#     <tbody class="Crom_body__UYOcU">
#         <tr>
#             <td class="Crom_text__NpR1_ Crom_sticky__uYvkp Crom_player__BuOU9">
#                 <a href="https://www.nba.com/stats/player/1641705/" class="Anchor_anchor__cSc3P" data-is-external="false" data-has-more="false" data-has-children="true">Victor Wembanyama</a>
#             </td>
#             <td class="Crom_text__NpR1_ Crom_primary__EajZu">
#                 <a href="https://www.nba.com/stats/team/1610612759/" class="Anchor_anchor__cSc3P" data-is-external="false" data-has-more="false" data-has-children="true">San Antonio Spurs</a>
#             </td>
#             <td class="Crom_text__NpR1_ Crom_primary__EajZu">Metropolitans 92 (France)</td>
#             <td>2023</td>
#             <td>1</td>
#             <td>1</td>
#             <td>1</td>
#         </tr>
#         <tr>
#             <td class="Crom_text__NpR1_ Crom_sticky__uYvkp Crom_player__BuOU9">
#                 <a href="https://www.nba.com/stats/player/1641706/" class="Anchor_anchor__cSc3P" data-is-external="false" data-has-more="false" data-has-children="true">Brandon Miller</a>
#             </td>
#             <td class="Crom_text__NpR1_ Crom_primary__EajZu">
#                 <a href="https://www.nba.com/stats/team/1610612766/" class="Anchor_anchor__cSc3P" data-is-external="false" data-has-more="false" data-has-children="true">Charlotte Hornets</a>
#             </td>
#             <td class="Crom_text__NpR1_ Crom_primary__EajZu">Alabama</td>
#             <td>2023</td>
#             <td>1</td>
#             <td>2</td>
#             <td>2</td>
#         </tr>
#         <tr>
#             <td class="Crom_text__NpR1_ Crom_sticky__uYvkp Crom_player__BuOU9">
#                 <a href="https://www.nba.com/stats/player/1630703/" class="Anchor_anchor__cSc3P" data-is-external="false" data-has-more="false" data-has-children="true">Scoot Henderson</a>
#             </td>
#             <td class="Crom_text__NpR1_ Crom_primary__EajZu">
#                 <a href="https://www.nba.com/stats/team/1610612757/" class="Anchor_anchor__cSc3P" data-is-external="false" data-has-more="false" data-has-children="true">Portland Trail Blazers</a>
#             </td>
#             <td class="Crom_text__NpR1_ Crom_primary__EajZu">Ignite (G League)</td>
#             <td>2023</td>
#             <td>1</td>
#             <td>3</td>
#             <td>3</td>
#         </tr>
#         <tr>
#             <td class="Crom_text__NpR1_ Crom_sticky__uYvkp Crom_player__BuOU9">
#                 <a href="https://www.nba.com/stats/player/1641708/" class="Anchor_anchor__cSc3P" data-is-external="false" data-has-more="false" data-has-children="true">Amen Thompson</a>
#             </td>
#             <td class="Crom_text__NpR1_ Crom_primary__EajZu">
#                 <a href="https://www.nba.com/stats/team/1610612745/" class="Anchor_anchor__cSc3P" data-is-external="false" data-has-more="false" data-has-children="true">Houston Rockets</a>
#             </td>
#             <td class="Crom_text__NpR1_ Crom_primary__EajZu">Overtime Elite</td>
#             <td>2023</td>
#             <td>1</td>
#             <td>4</td>
#             <td>4</td>
#         </tr>
#         <tr>
#             <td class="Crom_text__NpR1_ Crom_sticky__uYvkp Crom_player__BuOU9">
#                 <a href="https://www.nba.com/stats/player/1641709/" class="Anchor_anchor__cSc3P" data-is-external="false" data-has-more="false" data-has-children="true">Ausar Thompson</a>
#             </td>
#             <td class="Crom_text__NpR1_ Crom_primary__EajZu">
#                 <a href="https://www.nba.com/stats/team/1610612765/" class="Anchor_anchor__cSc3P" data-is-external="false" data-has-more="false" data-has-children="true">Detroit Pistons</a>
#             </td>
#             <td class="Crom_text__NpR1_ Crom_primary__EajZu">Overtime Elite</td>
#             <td>2023</td>
#             <td>1</td>
#             <td>5</td>
#             <td>5</td>
#         </tr>
#         <tr>
#             <td class="Crom_text__NpR1_ Crom_sticky__uYvkp Crom_player__BuOU9">
#                 <a href="https://www.nba.com/stats/player/1641710/" class="Anchor_anchor__cSc3P" data-is-external="false" data-has-more="false" data-has-children="true">Anthony Black</a>
#             </td>
#             <td class="Crom_text__NpR1_ Crom_primary__EajZu">
#                 <a href="https://www.nba.com/stats/team/1610612753/" class="Anchor_anchor__cSc3P" data-is-external="false" data-has-more="false" data-has-children="true">Orlando Magic</a>
#             </td>
#             <td class="Crom_text__NpR1_ Crom_primary__EajZu">Arkansas</td>
#             <td>2023</td>
#             <td>1</td>
#             <td>6</td>
#             <td>6</td>
#         </tr>