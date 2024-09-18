from fastapi import FastAPI
from app.api import sync, webhook, tasks

app = FastAPI()

app.include_router(sync.router)
app.include_router(webhook.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "FastAPI Data Warehouse"}
