from pydantic import BaseModel
import hashlib
import json

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