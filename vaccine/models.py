from ast import Index
from vaccine.database import Base
from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String

#ref https://fastapi.tiangolo.com/tutorial/body/

'''
##D2S #DataBase Entity. Mapping our codebase to DB
## created the model and defined all the fields that are suposed to be inside the table
#one model(Vaccine) connected to the table(vaccines).
#Vaccine is extended to the Base of db
##D2E
'''
class Vaccine(Base):
    __tablename__ = 'vaccines'
    vaccineId = Column(Integer, primary_key = True, index=True)
    startTime = Column(String)
    endTime   = Column(String)
