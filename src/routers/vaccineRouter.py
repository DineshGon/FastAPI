from fastapi import Depends, APIRouter, Response, HTTPException, status
from sqlalchemy.orm import Session
from src import database
from src.model import models

from src.repository import schemas, vaccineRepo

# Ref https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=bigger

router = APIRouter(

    prefix="/v1",
    tags=['vaccine']
)

get_db = database.get_db


@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Vaccine, db: Session = Depends(get_db)):
    # db: Session = Depends(get_db) convert session into pydantic thing
    # 1. we defined the db 2. it should be isntance or type of session.3. default values depends on db
    # once we do this we get the db instance
    return vaccineRepo.create_vaccine(request, db)


'''
Instead of getting a simple fields we are getting a request body in swagger.
Its a request model from pydantic model

@router.post('/vaccine')
def create(startTime,endTime):
    return {'starttime':startTime,'endtime': endTime}
'''


@router.delete('/{vaccineId}', status_code=status.HTTP_204_NO_CONTENT)
def deletevaccine(vaccineId, db: Session = Depends(get_db)):
    return vaccineRepo.delete_vaccine(vaccineId, db)


@router.put('/{vaccineId}', status_code=status.HTTP_202_ACCEPTED)
def update(vaccineId, request: schemas.Vaccine, db: Session = Depends(get_db)):
    return vaccineRepo.update_vaccine(vaccineId, request, db)


@router.get('/all')
def all(db: Session = Depends(get_db)):
    return vaccineRepo.get_all(db)


@router.get('/{vaccineId}', status_code=200)
def show(vaccineId, response: Response, db: Session = Depends(get_db)):
    return vaccineRepo.vaccine_byId(vaccineId, response, db)
