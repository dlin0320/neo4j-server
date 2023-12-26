from pydantic import BaseModel, Field
import hashlib
import time

class RetrieveArgs(BaseModel):
  address: str
  startTime: int = Field(0, ge=0)
  endTime: int = Field(time.time(), ge=0)
  minValue: int = Field(0, ge=0)
  maxValue: int = Field(9223372036854775807, ge=0)
  reverse: bool = Field(None)

def get_hash(obj: BaseModel) -> str:
  obj_dict = obj.model_dump()
  obj_str = str(sorted(obj_dict.items()))
  return hashlib.sha256(obj_str.encode()).hexdigest()