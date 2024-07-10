from enum import Enum


class ResponseContentType(Enum):
    TEXT_PLAIN = "text/plain; charset=utf-8"
    TEXT_HTML = 'text/html; charset=utf-8'
    APP_JSON = 'application/json'
