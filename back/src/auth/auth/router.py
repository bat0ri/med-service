from fastapi import APIRouter
from auth.schemas import UserInputSchema
from auth import service, security


router = APIRouter()


@router.post("/create", status_code=200)
async def registration(user: UserInputSchema):
    return await service.create_user(user)


@router.post('/login', status_code=200)
async def login(user: UserInputSchema):
    return await service.login_user(user)


@router.post('/validate', status_code=200)
async def protected(token: str):
    return security.decode_jwt(token)