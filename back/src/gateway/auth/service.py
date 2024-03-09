import httpx
from fastapi import HTTPException
from auth.schemas import TokenInput


async def get_all_users():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://0.0.0.0:8000/all")
        return response.json()



async def create_user(user):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://0.0.0.0:8000/auth/create", json=user)
        return response.json()



async def login_user(data: TokenInput):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://0.0.0.0:8000/auth/login", json=data)
        print(response.status_code)
        return response.json()

