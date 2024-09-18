from sqlalchemy.orm import Session
from app.models import Customer, Campaign
from app.schemas import CustomerBase, CampaignBase

def get_customers(db: Session, offset: int = 0, limit: int = 10):
    return db.query(Customer).offset(offset).limit(limit).all()

def get_campaigns(db: Session, offset: int = 0, limit: int = 10):
    return db.query(Campaign).offset(offset).limit(limit).all()

def create_customer(db: Session, customer: CustomerBase):
    db_customer = Customer(name=customer.name, email=customer.email)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def create_campaign(db: Session, campaign: CampaignBase):
    db_campaign = Campaign(title=campaign.title, status=campaign.status)
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign
