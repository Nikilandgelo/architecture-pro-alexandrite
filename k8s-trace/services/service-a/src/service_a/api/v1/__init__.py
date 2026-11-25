from fastapi import APIRouter
from .order import orders_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(orders_router, tags=["orders"])
