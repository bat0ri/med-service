from fastapi import APIRouter, HTTPException, Depends
from auth.service import get_all_users, create_user, login_user
from auth.schemas import UserInputSchema
from auth.protection import JWTBearer


auth = APIRouter(prefix='/auth', tags=['auth'])

@auth.get('/all')
async def all():
    return await get_all_users()



@auth.post('/registration')
async def registration(user: UserInputSchema):
    user_data = user.dict()
    return await create_user(user_data)


@auth.post('/login')
async def login(user: UserInputSchema):
    user_data = user.dict()
    return await login_user(data=user_data)


@auth.post('/validate', dependencies=[Depends(JWTBearer())])
async def validate():
    return "Token verified"