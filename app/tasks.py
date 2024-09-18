import httpx
from fastapi import HTTPException
from app.crud import create_customer, create_campaign

# Fetch customers from CRM API
async def fetch_customers(api_key: str):
    url = "https://challenge.berrydev.ai/api/crm/customers"
    headers = {"X-API-Key": api_key}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Error fetching CRM customers")

# Fetch campaigns from Marketing API
async def fetch_campaigns(api_key: str):
    url = "https://challenge.berrydev.ai/api/marketing/campaigns"
    headers = {"X-API-Key": api_key}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Error fetching Marketing campaigns")

# Background sync task
async def sync_data(source: str, api_key: str, db):
    if source == "crm":
        customers = await fetch_customers(api_key)
        for customer in customers:
            create_customer(db, customer)
    elif source == "marketing":
        campaigns = await fetch_campaigns(api_key)
        for campaign in campaigns:
            create_campaign(db, campaign)
    else:
        raise HTTPException(status_code=400, detail="Unknown source")
