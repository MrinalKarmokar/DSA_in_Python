import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Debug mode setting
DEBUG = True

# Application URLs
BASE_URL = "http://localhost:8000"
API_URL = f"{BASE_URL}/api"

# Database settings
DATABASE = {
    "ENGINE": "sqlite3",
    "NAME": os.path.join(os.path.dirname(os.path.abspath(__file__)), "db.sqlite3"),
}

# Logging settings
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG" if DEBUG else "INFO",
    },
}

# Allowed hosts
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Secret key
SECRET_KEY = "your-secret-key"