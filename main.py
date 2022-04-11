from operator import ipow
from sys import int_info
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


# creating an instance 
app =FastAPI()

@app.get("/all") #Path Operation Decorator @app 2. Operation on the path (get) 1. Path ("/") 
def base_index(limit =10, published :bool =True, sort: Optional[str] =None): # path operation function
    #Query parameters 
    if published:
        return {'data':f'{limit} vaccine users from db'}
    else :
        return {'data':f'{limit} not vaccinated from db'}

@app.get('/vaccine/{id}')
def show_vaccine_ids(id:int): # defining the type for the parameter
    return {'data':id}

@app.get('/vaccine/{id}/brands')
def show_brands(id):
    return {'data':{'1','2'}}

class Vaccine(BaseModel):
    vaccine_id: int
    start_time: str
    end_tim: str


@app.post("/vaccine")
def create_appointments(request: Vaccine):
    return {'data': f"vaccine appointment is created with {request.start_time}"}





# To chane th eport number in debugging
# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1", port= '9000')