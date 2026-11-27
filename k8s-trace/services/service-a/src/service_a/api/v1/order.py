from fastapi import APIRouter
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from service_a.http_clients import service_b_http_client

orders_router = APIRouter(prefix="/orders")

@orders_router.post("/")
async def make_order(request: Request):
    response = await service_b_http_client.get(url="/payments/check")
    return JSONResponse(
        content={
            "detail": "OK",
            "payments_response": response.json()
        },
        status_code=status.HTTP_200_OK
    )
