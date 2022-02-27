from fastapi import FastAPI
from api import router
from loguru import logger
from database.db_manager import metadata, engine, database

app = FastAPI()
app.include_router(router=router)


metadata.create_all(engine)
app.state.database = database



@app.get('/')
async def hello():
    return {'Info': {
        '1': '',
        '2': '',
        '3': '',
        '4': '',
        '5': ''
    }}

@app.on_event('startup')
async def on_startup():
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()
        logger.success('App started')

@app.on_event('shutdown')
async def on_shutdown():
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()
        logger.success('App shutdown')
