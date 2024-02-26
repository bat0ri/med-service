import httpx


async def get_all_users():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://users_fastapi:8000/all")
        response.raise_for_status()
        return response.json()