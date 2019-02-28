# coding: utf-8

import requests
from typing import Optional, Union
from ..exception.exception import IllegalResponseException


class Request:
    base_url = "http://api.wynncraft.com/public_api.php"
    user_agent = "Pynn/1.0 (Wynncraft API wrapper for Python: https://github.com/KashEight/Pynn)"

    def __init__(self, timeout: float = 10):
        self._timeout = timeout

    def call_api(self, data: Optional[dict], dict_return: bool = True) -> Union[dict, str]:
        header = {
            "User-Agent": self.user_agent
        }
        url = self.base_url + "?"

        if data:
            url += "&".join([f"{key}={value}" for key, value in data.items()])

        try:
            r = requests.get(url, headers=header, timeout=self._timeout)
            if r.status_code != 200:
                raise IllegalResponseException(r.status_code)

            if dict_return:
                return r.json()

            return r.text
        except (requests.exceptions.Timeout, IllegalResponseException) as e:
            print(e)
