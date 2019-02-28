# coding: utf-8

from .api import Wrapper


class Pynn:
    def __init__(self):
        self._timeout = 10

    @property
    def timeout(self) -> float:
        return self._timeout

    @timeout.setter
    def timeout(self, t: float):
        self._timeout = t

    def api(self) -> Wrapper:
        return Wrapper(timeout=self._timeout)
