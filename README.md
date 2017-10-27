# Introduction
Wynncraft API wrapper for Python3  

# How to use
```
from pynn import Pynn
client = Pynn()
```
All responses is "JSON" format.
## Requests
```
client.getGuildList()
    -> get guild-list.
client.getGuildStats(guilld="guildname")
    -> get guild-stats of "guildname".
client.getPlayerStats(player="playername (not uuid)")
    -> get player-stats, player argument must be being original.
client.getonlinePlayersSum()
    -> get total of online players.
client.getTerritoryList()
    -> get list of territory in Wynn-World.
client.getItemDB(category="category" or search="search")
    -> get item details on "category" or "search" data. (use either)
client.getStatsLead(type="type", timeframe="timeframe")
    -> get stats-leaderboards of "type" in "timeframe".
```
