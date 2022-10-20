from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from server.routes import router as BeerRouter

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    load_dotenv()
    app.mongodb_client = MongoClient(os.environ.get('Mongo_URL'))
    app.db = app.mongodb_client['Beer']


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(BeerRouter, tags=["beers"])
