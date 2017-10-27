# coding: utf-8
from pynn.request import Request
from pynn.exception import ArgumentException

class Wrapper:
    def __init__(self):
        self.request = Request

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

    def getItemDB(self, **kwargs):
        data = {
            "action": "itemDB"
        }
        if "category" in kwargs:
            data["category"] = kwargs["category"]
        elif "search" in kwargs:
            data["search"] = kwargs["search"]
        else:
            raise ArgumentException("Illegal args: {}".format(args for args in kwargs))
        return self.request.WynncraftAPI(data)

    def getStatsLead(self, type, timeframe):
        data = {
            "action": "statsLeaderBoard",
            "type": type,
            "timeframe": timeframe
        }
        return self.request.WynncraftAPI(data)