from fastapi import FastAPI
from auth.router import router
from auth.repository import UserRepository
import uvicorn
from fixtures.init_user import init_user_fixture


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await init_user_fixture()


@app.get('/')
def ping():
    return {
        'status': 200
    }

@app.get('/all')
async def all():
    return await UserRepository.get_all()


app.include_router(router=router, prefix='/auth', tags=['AUTH'])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)