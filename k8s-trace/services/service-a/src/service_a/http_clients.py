from httpx import AsyncClient

service_b_http_client = AsyncClient(base_url="http://service-b:9001/api/v1")


async def close_http_clients():
    await service_b_http_client.aclose()
    ...
