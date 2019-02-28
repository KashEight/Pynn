# coding: utf-8

from .request import Request
from typing import Union


class Wrapper:
    def __init__(self, timeout: float = 10):
        self.req = Request(timeout=timeout)

    def getGuildList(self, dict_return: bool = True) -> Union[dict, str]:
        data = {
            "action": "guildList"
        }
        return self.req.call_api(data=data, dict_return=dict_return)

    def getGuildStats(self, command: str, dict_return: bool = True) -> Union[dict, str]:
        data = {
            "action": "guildStats",
            "command": command
        }
        return self.req.call_api(data=data, dict_return=dict_return)

    def getPlayerStats(self, command: str, dict_return: bool = True) -> Union[dict, str]:
        data = {
            "action": "playerStats",
            "command": command
        }
        return self.req.call_api(data=data, dict_return=dict_return)

    def getOnlinePlayers(self, dict_return: bool = True) -> Union[dict, str]:
        data = {
            "action": "onlinePlayers"
        }
        return self.req.call_api(data=data, dict_return=dict_return)

    def getOnlinePlayersSum(self, dict_return: bool = True) -> Union[dict, str]:
        data = {
            "action": "onlinePlayersSum"
        }
        return self.req.call_api(data=data, dict_return=dict_return)

    def getTerritoryList(self, dict_return: bool = True) -> Union[dict, str]:
        data = {
            "action": "territoryList"
        }
        return self.req.call_api(data=data, dict_return=dict_return)

    def findItemByCategory(self, category: str, dict_return: bool = True) -> Union[dict, str]:
        data = {
            "action": "itemDB",
            "category": category
        }
        return self.req.call_api(data=data, dict_return=dict_return)

    def findItemByName(self, name: str, dict_return: bool = True) -> Union[dict, str]:
        data = {
            "action": "itemDB",
            "search": name
        }
        return self.req.call_api(data=data, dict_return=dict_return)

    def findStats(self, word: str, dict_return: bool = True) -> Union[dict, str]:
        data = {
            "action": "statsSearch",
            "search": word
        }
        return self.req.call_api(data=data, dict_return=dict_return)

    def getStatsLead(self, lead_type: str, timeframe: str, dict_return: bool = True) -> Union[dict, str]:
        data = {
            "action": "statsLeaderboard",
            "type": lead_type,
            "timeframe": timeframe
        }
        return self.req.call_api(data=data, dict_return=dict_return)
