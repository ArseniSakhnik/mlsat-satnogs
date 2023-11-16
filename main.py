from fastapi import FastAPI
import os
from dotenv import load_dotenv
from modules.mongodb.mongodb import MongodbContext

load_dotenv()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/test")
async def test():
    kal = MongodbContext()
    kal.test()
    token = os.getenv("SATNOGS_API_TOKEN")

