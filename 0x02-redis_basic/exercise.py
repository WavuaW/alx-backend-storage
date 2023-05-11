#!/usr/bin/env python3
import redis
import uuid
from typing import Union

class Cache:
    '''We are creating an object, Redis data store for data storage prposes 
    '''

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' In this case we are storing a value in the Redis data store and returning tht key.
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

