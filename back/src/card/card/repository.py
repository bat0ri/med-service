from fastapi import Depends
from sqlalchemy import select, delete, update, func
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from card.model import Card
from config import db



class CardRepository:

    @staticmethod
    async def insert(new_card: Card) -> Card:
        async with db as session:
            async with session.begin():
                session.add(new_card)
            await db.commit_rollback()


    @staticmethod
    async def get_all():
        async with db as session:
            query = select(Card)
            result = await session.execute(query)
            return result.scalars().all()


    @staticmethod
    async def get_by_id(id: str):
        async with db as session:
            query = select(Card).filter(Card.id==id)
            result = await session.execute(query)
            return result.scalars().first()


    @staticmethod
    async def drop_all():
        async with db as session:
            query = delete(Card)
            result = await session.execute(query)
            return await db.commit_rollback()