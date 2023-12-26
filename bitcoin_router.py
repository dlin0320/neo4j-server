from fastapi import APIRouter, Body
from cypher import Bitcoin_Cypher
from common import RetrieveArgs, get_hash
from client import bitcoin, cache
import json

bitcoin_router = APIRouter("/bitcoin")

@bitcoin_router.post("/transaction")
async def retrieve_transaction(args: RetrieveArgs = Body(...), page: int = None, limit: int = 20):
  hash = get_hash(args)
  resp = cache.get(hash)

  if resp:
    transactions = json.loads(resp)
    limit = min(100, limit)
    if page:
      return transactions[page * limit: (page + 1) * limit]

  query = Bitcoin_Cypher.retrieve_transaction(
    args.address,
    args.startTime,
    args.endTime,
    args.minValue,
    args.maxValue,
    args.reverse
  )

  resp = bitcoin.session().run(query)
  transactions = [record["result"] for record in resp]
  cache.set(hash, json.dumps(transactions), ex=60 * 60)
  return transactions[0:limit]