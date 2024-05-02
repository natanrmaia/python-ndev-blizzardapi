class HTTPException(Exception):
    """
    Represents an exception that occurs during an HTTP request.

    Attributes:
        code (int): The HTTP status code of the exception.
        message (str): The error message associated with the exception.
    """

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return f'HTTPException: {self.code} - {self.message}'

    def __repr__(self):
        return f'<HTTPException code={self.code} message={self.message}>'

    def __eq__(self, other):
        return self.code == other.code and self.message == other.message

    def __ne__(self, other):
        return not self.__eq__(other)

class HTTP400Error(HTTPException):
    """
    Represents an HTTP 400 error (Bad Request).
    Note: This error is raised when the request is invalid.
    """
    pass

class HTTP401Error(HTTPException):
    """
    Represents an HTTP 401 error (Unauthorized).
    Note: This error is raised when the client ID or client secret or access token is invalid.
    """
    pass

class HTTP403Error(HTTPException):
    """
    Represents an HTTP 403 error (Forbidden).
    Note: This error is raised when the client ID or client secret or access token is missing.
    """
    pass

class HTTP404Error(HTTPException):
    """
    Represents an HTTP 404 error (Not Found).
    Note: This error is raised when the API endpoint does not exist or results are not found.
    """
    pass

class HTTP429Error(HTTPException):
    """
    Represents an HTTP 429 error (Too Many Requests).
    Note: This error is raised when the rate limit is exceeded.
    """
    pass

class HTTP500Error(HTTPException):
    """
    Represents an HTTP 500 error (Internal Server Error).
    Note: This error is raised when the server encounters an unexpected condition.
    """
    pass

class HTTP503Error(HTTPException):
    """
    Represents an HTTP 503 error (Service Unavailable).
    Note: This error is raised when the server is unavailable.
    """
    pass

class HTTP504Error(HTTPException):
    """
    Represents an HTTP 504 error (Gateway Timeout).
    Note: This error is raised when the server is unavailable.
    """
    pass

class HTTPUnknownError(HTTPException):
    """
    Represents an unknown HTTP error.
    Note: This error is raised when an unknown error occurs.
    """
    pass