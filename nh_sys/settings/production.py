from nh_sys.settings.base import (
    ALLOWED_HOSTS,
    CORS_ALLOWED_ORIGIN_REGEXES,
    CORS_ALLOWED_ORIGINS,
)

DEBUG = False

ALLOWED_HOSTS += [
    "api-nh_sys.herokuapp.com",
]

CORS_ALLOWED_ORIGINS += [
    "https://nh_sys.netlify.app",
]


CORS_ALLOWED_ORIGIN_REGEXES += [
    r"^https:\/\/*\.nh_sys\.co\.ke",
    r"(^|^[^:]+:\/\/|[^\.]+\.)nh_sys\.co\.ke",
]
