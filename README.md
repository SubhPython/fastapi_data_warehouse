# FastAPI Data Warehouse

This project is a FastAPI application that collects and synchronizes data from external APIs and handles webhooks.

## Features
- Webhook handling
- Data synchronization from multiple external APIs
- Background task management
- SQLite for data storage

## Endpoints

- POST `/webhook`: Receive data from a webhook.
- GET `/sync/{source}`: Start synchronization for a data source.
- GET `/data`: Retrieve stored data with pagination.
- GET `/tasks`: List all running background tasks.
- POST `/tasks/cancel`: Cancel a specific background task.

## Setup Instructions

```bash
git clone <repository-url>
cd fastapi_data_warehouse
pip install -r requirements.txt
uvicorn app.main:app --reload
