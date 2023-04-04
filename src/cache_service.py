import redis
from bin.constants import REDIS_CONFIG

r = redis.Redis(**REDIS_CONFIG)