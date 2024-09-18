from fastapi import APIRouter, BackgroundTasks, Header, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.tasks import sync_data
from app.crud import get_customers, get_campaigns
from app.schemas import WebhookData

router = APIRouter()

# Webhook endpoint
@router.post("/webhook")
async def webhook_endpoint(webhook: WebhookData):
    return {"message": "Webhook received"}

# Get data with pagination
@router.get("/data")
async def get_data(offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    customers = get_customers(db, offset=offset, limit=limit)
    campaigns = get_campaigns(db, offset=offset, limit=limit)
    return {"customers": customers, "campaigns": campaigns}

# Sync endpoint
@router.get("/sync/{source}")
async def sync_source(source: str, background_tasks: BackgroundTasks, api_key: str = Header(None), db: Session = Depends(get_db)):
    background_tasks.add_task(sync_data, source, api_key, db)
    return {"message": f"Sync initiated for {source}"}
