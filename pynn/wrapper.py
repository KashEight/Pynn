# coding=utf-8
from pynn.request import Request
from pynn.exception import ArgumentException

class Wrapper:
    def __init__(self):
        self.request = Request()

    def getGuildList(self):
        data = {
            "action": "guildList"
        }
        return self.request.WynncraftAPI(data)

    def getGuildStats(self, guild):
        data = {
            "action": "guildStats",
            "command": guild
        }
        return self.request.WynncraftAPI(data)

    def getPlayerStats(self, player):
        data = {
            "action": "playerStats",
            "command": player
        }
        return self.request.WynncraftAPI(data)

    def getonlinePlayersSum(self):
        data = {
            "action": "onlinePlayersSum"
        }
        return self.request.WynncraftAPI(data)

    def getTerritoryList(self):
        data = {
            "action": "territoryList"
        }
        return self.request.WynncraftAPI(data)

    def getItemDB(self, category=None, search=None):
        data = {
            "action": "itemDB"
        }
        if not (category and search):
            raise ArgumentException("There is no argument in category and search.")
        elif category and search:
            raise ArgumentException("Select argument either, category or search.")
        elif category:
            data["category"] = category
        elif search:
            data["search"] = search
        return self.request.WynncraftAPI(data)

    def getStatsLead(self, type, timeframe):
        data = {
            "action": "statsLeaderBoard",
            "type": type,
            "timeframe": timeframe
        }
        return self.request.WynncraftAPI(data)