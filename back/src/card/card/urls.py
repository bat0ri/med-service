from fastapi import APIRouter
from card.repository import CardRepository
from card.schemas import CardInput
from card.model import Card

router = APIRouter(prefix='/card', tags=["Card's endpoints"])



@router.get('/list')
async def get_all_cards():
    return await CardRepository.get_all()


@router.post('/create')
async def create_card(card: CardInput):
    new_card = Card(name=card.name)
    return await CardRepository.insert(new_card)