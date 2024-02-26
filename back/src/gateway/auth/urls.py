from fastapi import APIRouter


auth = APIRouter(prefix='/auth', tags=['auth'])

@auth.get('/all')
async def all():
    return await get_all_users()