

from ast import Index
from .database import Base
from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String


class Vaccine(Base):
    __tablename__ = 'vaccines'
    vaccineId = Column(Integer, primary_key = True, index=True)
    startTime = Column(String)
    endTime   = Column(String)
