from decouple import config

from .base import *  # noqa F403, F401

env = config("ENVIRONMENT", "local")

if env == "production":
    from .production import *  # noqa F403, F401

elif env == "staging":
    from .staging import *  # noqa F403, F401

else:
    from .local import *  # noqa F403, F401
