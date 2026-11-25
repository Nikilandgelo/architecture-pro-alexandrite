import asyncio

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from starlette import status
from starlette.requests import Request

payments_router = APIRouter(prefix="/payments")

@payments_router.get("/check")
async def check_payments(request: Request):
    await asyncio.sleep(1)
    return JSONResponse(
        content={"status": "success"},
        status_code=status.HTTP_200_OK
    )
