from fastapi import Depends, FastAPI
from dotenv import load_dotenv
from typing import Annotated
from modules.satnogs_api.satnogs_api import SatnogsApiService

load_dotenv()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/api/initialize-basic-encoders")
async def initialize_basic_encodes(satnogs_api_service: Annotated[SatnogsApiService, Depends(SatnogsApiService)]):
    return satnogs_api_service.initialize_basic_decoders()


@app.post("/api/initialize-raw-data")
async def initialize_raw_data(satnogs_api_service: Annotated[SatnogsApiService, Depends(SatnogsApiService)]):
    return satnogs_api_service.initialize_raw_data()
