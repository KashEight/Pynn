# coding; utf-8


class PynnException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message


class IllegalArgumentException(PynnException):
    """
    Occur when an argument is illegal.
    """


class APIException(PynnException):
    """
    Abstract Exception Class.
    """


class IllegalResponseException(APIException):
    def __init__(self, status_code: int):
        super().__init__(f"Response was not correct: {str(status_code)}")

