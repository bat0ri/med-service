from fastapi import FastAPI, Request, Depends
import uvicorn
import httpx
from fastapi.middleware.cors import CORSMiddleware

from auth.urls import auth
from auth.protection import JWTBearer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth)

@app.get('/protected', dependencies=[Depends(JWTBearer())])
async def hello(request: Request):
    return 'hello'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7000)