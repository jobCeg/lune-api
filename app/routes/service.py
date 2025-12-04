from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/error400")
async def trigger_400():
    raise HTTPException(status_code=400, detail="This is a bad request")

@router.get("/error404")
async def trigger_404():
    raise HTTPException(status_code=404, detail="Resource not found")

@router.get("/error500")
async def trigger_500():
    raise Exception("Unexpected error")

