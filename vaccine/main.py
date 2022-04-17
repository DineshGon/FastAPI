from fastapi import Depends, FastAPI, status, Response, HTTPException
# from rootmain import Vaccine

from vaccine.database import SessionLocal
from vaccine import schemas, models
from vaccine.database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from vaccine.routers import vaccineRouter

app = FastAPI()

"""D3S
Below line creates a table in DB
Whenever we are running the server we are going to create all the models into the db.
we can simply say creating the tables. this is happening everytime.
if table is there then its not going to do anything. if table is not there it will going to create it 
"""
models.Base.metadata.create_all(engine)


##D3E

@app.get("/helloworld", tags=["DevSecOps"])
async def hello_world():
    return {"msg": "Hello World"}


'''
with this you can write main.py in separate files
'''
app.include_router(vaccineRouter.router)

# -----------------------------------------------------------------------------------------------
# def get_db():
#     db =SessionLocal() # from the db
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post('/vaccine' , status_code=status.HTTP_201_CREATED, tags =['vaccine'])
# def create(request: schemas.Vaccine, db: Session = Depends(get_db)): 
#     # db: Session = Depends(get_db) convert session into pydantic thing
#    new_vac = models.Vaccine(startTime= request.startTime, endTime = request.endTime) #vaccineId = request.vaccineId, 
#    db.add(new_vac)
#    db.commit()
#    db.refresh(new_vac)
#    return new_vac


# @app.delete('/vaccine/{vaccineId}', status_code= status.HTTP_204_NO_CONTENT,tags =['vaccine'])
# def deletevaccine(vaccineId, db: Session = Depends(get_db)):
#     # db.query(models.Vaccine).filter(models.Vaccine.vaccineId == vaccineId).delete(synchronize_session= False)
#     # db.commit()
#     # return 'done'

#     delbyid = db.query(models.Vaccine).filter(models.Vaccine.vaccineId == vaccineId)

#     if not delbyid.first():
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Vaacine id  {vaccineId} not found")

#     delbyid.delete(synchronize_session= False)
#     db.commit()
#     return 'done'

# @app.put('/vaccine/{vaccineId}', status_code= status.HTTP_202_ACCEPTED, tags =['vaccine'])
# def update(vaccineId, request: schemas.Vaccine, db: Session = Depends(get_db)):
#     #preparing the query 
#     vacbyid = db.query(models.Vaccine).filter(models.Vaccine.vaccineId == vaccineId)
#     # if there is id give me the first one 
#     if not vacbyid.first():
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Vaacine id  {vaccineId} not found")

#     vacbyid.update(request.dict()) 
#     # vacbyid.update({'startTime':request.startTime,'endTime' :request.endTime})
#     db.commit()
#     return 'updated'
#     # First approach
#     # db.query(models.Vaccine).filter(models.Vaccine.vaccineId == vaccineId).update({'startTime': 'start Time updated'})
#     # db.commit()
#     # return 'updated'
#     #2nd app
#     # print(schemas.Vaccine)
#     # db.query(models.Vaccine).filter(models.Vaccine.vaccineId == vaccineId).update(request)
#     # db.commit()
#     # return 'updated'


# @app.get('/vaccine', tags =['vaccine'])
# def all(db: Session = Depends(get_db)):
#     allvaccines = db.query(models.Vaccine).all()
#     return allvaccines


# @app.get('/vaccine/{vaccineId}', status_code= 200, tags =['vaccine'])
# def show(vaccineId, response: Response, db: Session = Depends(get_db)):
#     vaccinesbyid = db.query(models.Vaccine).filter(models.Vaccine.vaccineId ==vaccineId).first()
#     if not vaccinesbyid:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#          detail=f"user with the vaccineId {vaccineId} not available")
#         # response.status_code =status.HTTP_404_NOT_FOUND
#         # return {'detail' : f"user with the vaccineId{vaccineId} not found"}
#     return vaccinesbyid
