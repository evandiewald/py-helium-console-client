from requests import Response
import json


class AuthenticationError(Exception):
    """Raised when the provided API Key is not valid"""
    pass


class InvalidQueryError(Exception):
    """Raised when a query parameter is not found"""
    pass


def check_response(r: Response):
    if r.status_code == 401:
        raise AuthenticationError(r.text)
    elif r.status_code == 404:
        raise InvalidQueryError(r.text)
    elif r.status_code == 400:
        raise InvalidQueryError(r.text)
    try:
        return r.json()
    except json.decoder.JSONDecodeError:
        return r
