from fastapi import FastAPI
from app.api import endpoints

app = FastAPI(title="FastAPI Data Warehouse", version="1.0.0")

app.include_router(endpoints.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Data Warehouse!"}
