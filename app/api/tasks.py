from fastapi import APIRouter

router = APIRouter()

@router.get("/tasks")
async def list_tasks():
    # List all running tasks (mock)
    return {"tasks": ["sync_task_1", "sync_task_2"]}

@router.post("/tasks/cancel")
async def cancel_task(task_id: str):
    # Logic to cancel the task
    return {"message": f"Task {task_id} cancelled"}
