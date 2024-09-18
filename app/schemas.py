from pydantic import BaseModel

class WebhookData(BaseModel):
    event_type: str
    data: dict

class CustomerBase(BaseModel):
    name: str
    email: str

class CampaignBase(BaseModel):
    title: str
    status: str
