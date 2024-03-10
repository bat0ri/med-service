from fastapi import APIRouter
from appoint.repository import AppointRepository
from appoint.schemas import CreateAppoint
from appoint.model import Appoint


router = APIRouter(prefix='/appoint', tags=["Appoint endpoints"])


@router.post('/create')
async def create_appoints(appoint: CreateAppoint):
    new_appoint = Appoint(user_id=appoint.user_id,
                            doctor_id=appoint.doctor_id,
                            date=appoint.date)
    return await AppointRepository.insert(new_appoint)


@router.get('/list')
async def get_appoint_list():
    return await AppointRepository.get_all()

@router.get('/get')
async def get_appoint(id: str):
    return await AppointRepository.get_by_id(id)
    