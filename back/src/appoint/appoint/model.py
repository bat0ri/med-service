from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
import datetime
import uuid


Base = declarative_base()


class Appoint(Base):

    __tablename__ = 'appoints'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    user_id = Column(String, nullable=False)
    doctor_id = Column(String, nullable=False)
    # время записи к врачу
    date = Column(DateTime, nullable= False)

    create_date = Column(DateTime, default=datetime.datetime.now(), nullable= True)