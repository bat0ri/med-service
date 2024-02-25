from fastapi import FastAPI
import uvicorn
import httpx

app = FastAPI()


async def get_all_users():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://users_fastapi:8000/all")
        response.raise_for_status()
        return response.json()


@app.get('/all')
async def all():
    return await get_all_users()



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7000)