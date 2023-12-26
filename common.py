from pydantic import BaseModel, Field
from dotenv import load_dotenv
import hashlib
import time
import json
import os

load_dotenv()
BITCOIN_NEO4J = os.environ.get('BITCOIN_NEO4J')
ETHEREUM_NEO4J = os.environ.get('ETHEREUM_NEO4J')
TRON_NEO4J = os.environ.get('TRON_NEO4J')
NEO4J_READER = os.environ.get('NEO4J_READER')
READER_PASSWORD = os.environ.get('READER_PASSWORD')

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

def get_database(chain, timestamp):
  with open("database.json", "r") as database:
    databases = json.load(database)[chain]
    for database in databases:
      start = database["startTime"]
      end = database["endTime"]
      if start <= timestamp and timestamp <= end:
        return database["name"]