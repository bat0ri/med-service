from fastapi import FastAPI
from appoint.router import router

app = FastAPI()


@app.get('/')
def pint():
    return {
        'service': 'Appoint'
    }

app.include_router(router)