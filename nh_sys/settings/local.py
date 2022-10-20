from nh_sys.settings.base import (
    ALLOWED_HOSTS,
    CORS_ALLOWED_ORIGIN_REGEXES,
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS += [
    "127.0.0.1",
    "localhost",
]

CORS_ALLOWED_ORIGIN_REGEXES += [
    r"^(http?:\/\/)?((localhost)|(127\.0\.0\.1)):3\d{3}",
]
