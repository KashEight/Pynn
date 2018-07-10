# coding: utf-8


class BaseException(Exception):
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, self.message)

    def __str__(self):
        return self.message


class APIError(BaseException):
    """
    Cause when APIs are illegal.
    """


class ArgumentException(BaseException):
    """
    Cause when arguments are illegal.
    """
