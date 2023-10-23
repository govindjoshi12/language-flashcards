from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    OPENSUB_KEY=environ.get("OPEN_SUBTITLES_API_KEY")

class ProdConfig(Config):
    FLASK_ENV='production'
    DEBUG=False
    TESTING=False

class DevConfig(Config):
    FLASK_ENV='development'
    DEBUG=True
    TESTING=True

    OPENSUB_USER=environ.get("OPEN_SUBTITLES_USERNAME")
    OPENSUB_PASS=environ.get("OPEN_SUBTITLES_PASSWORD")
