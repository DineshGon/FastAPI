from pydantic import BaseModel

"""
Instead of getting a simple fields we are getting a request body in swagger.
Its a request model from pydantic model

"""


class Vaccine(BaseModel):
    # vaccineId: int
    startTime: str
    endTime: str
