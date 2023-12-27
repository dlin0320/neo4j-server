from pydantic import BaseModel, Field
from dotenv import load_dotenv
import time
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

class GraphArgs(BaseModel):
  address: str
  timespan: int = Field(604800, ge=0)
  maxRelationshipCount: int = Field(3, ge=0)
  startTime: int = Field(0, ge=0)
  endTime: int = Field(time.time(), ge=0)
  minValue: int = Field(0, ge=0)
  maxValue: int = Field(9223372036854775807, ge=0)
  depth: int = Field(5, ge=0)
  reverse: bool = Field(None)