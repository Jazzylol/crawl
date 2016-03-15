import redis

from .. import settings


class RedisHelper:
    def __init__(self):
        self.host = settings.REDIS_SERVER
        self.port = settings.REDIS_PORT
        try:
            self.client = redis.StrictRedis(host=self.host, port=self.port)
        except Exception, exception:
            print exception

    def set_obj(self, key, val):
        try:
            self.client.set(key, val)
        except Exception, exception:
            print exception
