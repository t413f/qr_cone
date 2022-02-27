import databases
import sqlalchemy
from settings import settings

metadata = sqlalchemy.MetaData()
database = databases.Database(settings.database_url)
engine = sqlalchemy.create_engine(settings.database_url)