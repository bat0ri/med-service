from fastapi import Depends
from sqlalchemy import select, delete, update, func
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from appoint.model import Appoint
from config import db



class AppointRepository:


    @staticmethod
    async def insert(new_appoint: Appoint) -> Appoint:
        async with db as session:
            async with session.begin():
                session.add(new_appoint)
            await db.commit_rollback()


    @staticmethod
    async def get_all():
        async with db as session:
            query = select(Appoint)
            result = await session.execute(query)
            return result.scalars().all()


    @staticmethod
    async def get_by_id(id: str):
        async with db as session:
            query = select(Appoint).filter(Appoint.id==id)
            result = await session.execute(query)
            return result.scalars().first()