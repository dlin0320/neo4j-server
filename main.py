from bitcoin_router import bitcoin_router
from ethereum_router import ethereum_router
from tron_router import tron_router
from fastapi import FastAPI, HTTPException
from logging import getLogger

logger = getLogger(__name__)

app = FastAPI()

@app.exception_handler(Exception)
async def handle_exception(_, exc):
  logger.exception(exc)
  return HTTPException(status_code=500, detail=str(exc))

app.include_router(bitcoin_router)

app.include_router(ethereum_router)

app.include_router(tron_router)

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000)