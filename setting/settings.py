import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TITLE = os.getenv("TITLE", "Healthchecks.io")
PROJECTS = os.getenv("PROJECTS")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DOMAIN_NAME = os.getenv("DOMAIN_NAME", None)

if ( BASE_DIR / "setting/local_settings.py" ).exists():
    from .local_settings import *