from fastapi import APIRouter, BackgroundTasks
import asyncio

router = APIRouter()

@router.get("/sync/{source}")
async def sync_data(source: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(sync_source_data, source)
    return {"message": f"Synchronization for {source} started"}

async def sync_source_data(source: str):
    await asyncio.sleep(2)  # Simulate sync delay
    # Logic to fetch and store data from external APIs
    print(f"Data synchronization complete for {source}")
