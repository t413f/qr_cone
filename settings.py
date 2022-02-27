from pydantic import BaseSettings

class Settings(BaseSettings):
    hostname = '127.0.0.1'
    portname = 6000
    database_url = 'sqlite:///db.db'

settings = Settings()