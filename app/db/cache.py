import os

import redis
from fastapi import Depends
from typing import Annotated

def get_cache():
    # Create a Redis client
    cache = redis.Redis(
      host='honest-zebra-50522.upstash.io',
      port=6379,
      password=os.getenv("REDIS_PASSWORD"),
      ssl=True
    )
    return cache


cache_dependency = Annotated[None, Depends(get_cache)]
