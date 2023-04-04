import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY = os.environ["LIBRARY_OF_CONGRESS_API_KEY"]

REDIS_CONFIG = {
    "host": "localhost",
    "port": 6379,
    "decode_responses": True
}