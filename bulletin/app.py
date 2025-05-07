from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import router

from dotenv import load_dotenv

app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)