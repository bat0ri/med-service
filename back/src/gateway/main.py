from fastapi import FastAPI
import uvicorn
import httpx


from auth.urls import auth

app = FastAPI()

app.include_router(auth)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7000)