from neo4j import GraphDatabase
import redis
import os

BITCOIN_NEO4J = os.environ.get('BITCOIN_NEO4J')
ETHEREUM_NEO4J = os.environ.get('ETHEREUM_NEO4J')
TRON_NEO4J = os.environ.get('TRON_NEO4J')
NEO4J_READER = os.environ.get('NEO4J_READER')
READER_PASSWORD = os.environ.get('READER_PASSWORD')

bitcoin = GraphDatabase.driver(BITCOIN_NEO4J, auth=(NEO4J_READER, READER_PASSWORD))

ethereum = GraphDatabase.driver(ETHEREUM_NEO4J, auth=(NEO4J_READER, READER_PASSWORD))

tron = GraphDatabase.driver(TRON_NEO4J, auth=(NEO4J_READER, READER_PASSWORD))

cache = redis.Redis(host='redis', port=6379, db=0)