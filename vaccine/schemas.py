from pydantic import BaseModel


class Vaccine(BaseModel):
    # vaccineId: int
    startTime: str
    endTime: str