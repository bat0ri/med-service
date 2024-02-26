from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
import datetime
import uuid


Base = declarative_base()


class Card(Base):

    __tablename__ = 'cards'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    name = Column(String, nullable= False)
    create_date = Column(DateTime, default=datetime.datetime.now(), nullable= True)
