# Introduction
Wynncraft API wrapper for Python3  

# Usage
```
from pynn import Pynn
client = Pynn()
```
All responses is "JSON" format.  
The details are written [here](https://forums.wynncraft.com/threads/wynncraft-public-api.127085/).

## Requests
```
client.getGuildList()
    -> get guild list.
    
client.getGuildStats(guild="guildname")
    -> get guild stats of "guildname".
    
client.getPlayerStats(player="playername (not uuid)")
    -> get player stats (player argument must be original.)
    
client.getonlinePlayersSum()
    -> get total of online players.
    
client.getTerritoryList()
    -> get list of territory in Wynn-World.
    
client.getItemDB(category="category" or search="search")
    -> get item details on "category" or "search" data. (use either.)
    
client.getStatsLead(type="type", timeframe="timeframe")
    -> get stats-leaderboards of "type" in "timeframe".
```
