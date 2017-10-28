# coding=utf-8
import requests
from pynn.exception import APIError

class Request:

    baseUrl = "http://api.wynncraft.com/public_api.php?"
    userAgent = "Pynn/1.0 (Wynncraft API wrapper for Python; https://github.com/KashEight/Pynn)"
    timeout = 10

    def __call(self, url, header):
        try:
            response = requests.get(url, headers=header, timeout=self.timeout)
            if response.status_code != 200:
                raise APIError("API returned `{}`. Response was `{}`.".format(response.status_code, response.text))
        except requests.exceptions.Timeout:
            raise APIError("Request timed out. ({} secs)".format(self.timeout))
        try:
            return response.json()
        except:
            raise APIError("Could not decode response json. Response was `{}`.".format(response.text))

    def WynncraftAPI(self, data=None):
        if not data:
            data = {}
        url = self.baseUrl
        if data:
            url += "&".join(["{}={}".format(key, value) for key, value in data.items()])
        header = {
            "User-Agent": self.userAgent
        }
        return self.__call(url, header)