from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/webhook")
async def receive_webhook(request: Request):
    payload = await request.json()
    # Process the webhook payload
    return {"message": "Webhook received", "payload": payload}
