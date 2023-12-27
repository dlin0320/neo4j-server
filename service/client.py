from common.constant import BITCOIN_NEO4J, ETHEREUM_NEO4J, TRON_NEO4J, NEO4J_READER, READER_PASSWORD
from neo4j import GraphDatabase
import redis

bitcoin = GraphDatabase.driver(BITCOIN_NEO4J, auth=(NEO4J_READER, READER_PASSWORD))

ethereum = GraphDatabase.driver(ETHEREUM_NEO4J, auth=(NEO4J_READER, READER_PASSWORD))

tron = GraphDatabase.driver(TRON_NEO4J, auth=(NEO4J_READER, READER_PASSWORD))

retrieve_cache = redis.Redis(db=0)

graph_cache = redis.Redis(db=1)