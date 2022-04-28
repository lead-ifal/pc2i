from pydantic import BaseModel, Field
from werkzeug.datastructures import FileStorage
from typing import Optional
from datetime import datetime
from app.models.objectid import PydanticObjectId

class Culture(BaseModel):
  id: Optional[PydanticObjectId] = Field(alias="_id")
  zone_id: str
  name: str
  type: str
  planting_date: datetime
  harvest_date: datetime
  coefficient_et: float
  phase: str
  geographic_coordinates: dict
  image: FileStorage

  class Config:
    arbitrary_types_allowed = True
