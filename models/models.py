import ormar
import datetime
from database.db_manager import metadata, database


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Users(ormar.Model):
    class Meta(MainMeta):
        pass
    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=50)
    create_at: datetime.date = ormar.DateTime(default=datetime.datetime.now())


class QR_gen(ormar.Model):
    class Meta(MainMeta):
        pass
    id: int = ormar.Integer(primary_key=True)
    user: str = ormar.String(max_length=50)
    create_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now())
    content: str = ormar.String(max_length=200)
    fileb64: str = ormar.String()
