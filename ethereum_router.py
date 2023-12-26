from fastapi import APIRouter, Body
from cypher import Ethereum_Cypher
from common import RetrieveArgs, get_hash
from client import ethereum, cache
import json

ethereum_router = APIRouter("/ethereum")

@ethereum_router.post("/transaction")
def retrieve_transaction(args: RetrieveArgs = Body(...), page: int = None, limit: int = 20):
  hash = get_hash(args)
  resp = cache.get(hash)

  if resp:
    transactions = json.loads(resp)
    limit = min(100, limit)
    if page:
      return transactions[page * limit: (page + 1) * limit]
    
  query = Ethereum_Cypher.retrieve_transaction(
    args.address,
    args.startTime,
    args.endTime,
    args.minValue,
    args.maxValue,
    args.reverse
  )

  resp = ethereum.session().run(query)
  transactions = [record["result"] for record in resp]
  cache.set(hash, json.dumps(transactions), ex=60 * 60)
  return transactions[0:limit]

@ethereum_router.post("/tokenTransfer")
def retrieve_token_transfer(args: RetrieveArgs = Body(...), page: int = None, limit: int = 20):
  hahs = get_hash(args)
  resp = cache.get(hash)

  if resp:
    transactions = json.loads(resp)
    limit = min(100, limit)
    if page:
      return transactions[page * limit: (page + 1) * limit]
    
  query = Ethereum_Cypher.retrieve_token_transfer(
    args.address,
    args.startTime,
    args.endTime,
    args.minValue,
    args.maxValue,
    args.reverse
  )

  resp = ethereum.session().run(query)
  transactions = [record["result"] for record in resp]
  cache.set(hash, json.dumps(transactions), ex=60 * 60)
  return transactions[0:limit]