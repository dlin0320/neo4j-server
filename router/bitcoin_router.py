import logging
from common.utility import get_hash, get_database
from common.constant import RetrieveArgs, GraphArgs
from cypher.bitcoin_cypher import *
from fastapi import APIRouter, Body
from service import bitcoin, retrieve_cache, graph_cache
import json

bitcoin_router = APIRouter(prefix="/bitcoin")

bitcoin_database = lambda timestamp: get_database("bitcoin", timestamp)

logging.basicConfig(filename='debug.log', level=logging.INFO, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

@bitcoin_router.post("/transaction")
def retrieve_transaction(args: RetrieveArgs = Body(...), page: int = None, limit: int = 20):
  hash = get_hash(args)
  resp = retrieve_cache.get(hash)

  if resp:
    transactions = json.loads(resp)
    limit = min(100, limit)
    if page:
      return transactions[page * limit: (page + 1) * limit]

  query = retrieve_transaction_query(
    args.address,
    args.startTime,
    args.endTime,
    args.minValue,
    args.maxValue,
    args.reverse
  )

  start_database = bitcoin_database(args.startTime)
  # end_database = bitcoin_database(args.endTime)
  # if start_database != end_database:
  #   start_resp = bitcoin.session(database=start_database).run(query)
  #   end_resp = bitcoin.session(database=end_database).run(query)
  #   transactions = [record["result"] for record in start_resp] + [record["result"] for record in end_resp]
  #   transactions.sort(key=lambda x: x["timestamp"])
  #   retrieve_cache.set(hash, json.dumps(transactions), ex=60 * 60)
  #   return transactions[0:limit]

  resp = bitcoin.session(database=start_database).run(query)
  transactions = [record["result"] for record in resp]
  retrieve_cache.set(hash, json.dumps(transactions), ex=60 * 60)
  return transactions[0:limit]

@bitcoin_router.post("/graph")
def graph_transaction(args: GraphArgs = Body(...)):
  hash = get_hash(args)
  resp = graph_cache.get(hash)

  if resp:
    transactions = json.loads(resp)

  query = graph_transaction_query(
    args.address,
    args.timespan,
    args.maxRelationshipCount,
    args.startTime,
    args.minValue,
    args.maxValue,
    args.depth * 2,
    args.reverse
  )

  start_database = bitcoin_database(args.startTime)
  # end_database = bitcoin_database(args.endTime)
  # if start_database != end_database:
  #   start_resp = bitcoin.session(database=start_database).run(query)
  #   end_resp = bitcoin.session(database=end_database).run(query)
  #   transactions = [record["result"] for record in start_resp] + [record["result"] for record in end_resp]
  #   transactions.sort(key=lambda x: x["timestamp"])
  #   retrieve_cache.set(hash, json.dumps(transactions), ex=60 * 60)
  #   return transactions

  resp = bitcoin.session(database=start_database).run(query)
  transactions = [record["result"] for record in resp]
  retrieve_cache.set(hash, json.dumps(transactions), ex=60 * 60)
  logger.info(f"args: {args}")
  logger.info(f"transaction: {transactions}")
  return transactions