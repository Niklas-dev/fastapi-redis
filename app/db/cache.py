import redis
from fastapi import Depends


def get_cache():
    # Create a Redis client
    cache = redis.Redis(
        host='localhost',  # Redis server address
        port=6379,  # Redis server port
        db=0,  # Redis database index
        decode_responses=True  # Ensure the response is decoded to string
    )
    return cache


cache_dependency = Depends(get_cache)
