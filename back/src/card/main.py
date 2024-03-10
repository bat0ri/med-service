from fastapi import FastAPI
import uvicorn

from card.router import router 

app = FastAPI()

@app.get('/')
def ping():
    return {'status': 'OK'}

app.include_router(router)


if __name__=="__main__":
    uvicorn.run(app=app, host='0.0.0.0', port=8001)