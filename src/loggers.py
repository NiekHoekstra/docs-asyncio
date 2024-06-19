from logging.config import dictConfig

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{name}({levelname}): {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            # "stream": "ext://sys.stdout",
            "formatter": "simple"
        },
    },
    "loggers": {
        "root": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "asyncio": {
            "level": "DEBUG"
        }
    },
}
dictConfig(LOGGING)
