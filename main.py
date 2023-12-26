from fastapi import FastAPI, HTTPException
from logging import getLogger

logger = getLogger(__name__)

app = FastAPI()

@app.exception_handler(Exception)
async def handle_exception(_, exc):
  logger.exception(exc)
  return HTTPException(status_code=500, detail=str(exc))

@app.get("/tron/transaction")
def read_root():
  return {"Hello": "World"}