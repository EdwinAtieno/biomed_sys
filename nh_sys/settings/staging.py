from nh_sys.settings.base import (
    ALLOWED_HOSTS,
    CORS_ALLOWED_ORIGIN_REGEXES,
    CORS_ALLOWED_ORIGINS,
)

DEBUG = True

ALLOWED_HOSTS += [
    ".herokuapp.com",
]

CORS_ALLOWED_ORIGINS += [
    "https://nh_sys-fend-pwa.herokuapp.com",
    "https://nh_sys-proxy.herokuapp.com",
]

CORS_ALLOWED_ORIGIN_REGEXES += [
    r"^(http?:\/\/)?((localhost)|(127\.0\.0\.1)):3\d{3}",
    r"^(http?:\/\/)?((localhost)|(127\.0\.0\.1)):5\d{3}",
    r"^https:\/\/nh_sys-*",
    r"(^|^[^:]+:\/\/|[^\.]+\.)nh_sys\.co\.ke",
]