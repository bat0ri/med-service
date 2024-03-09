from fastapi import FastAPI
import uvicorn
import httpx
from fastapi.middleware.cors import CORSMiddleware

from auth.urls import auth

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7000)