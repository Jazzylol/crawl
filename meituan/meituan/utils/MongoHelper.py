import pymongo as pymongo

from .. import settings


class MongoHelper(object):
    def __init__(self):
        self.server = settings.MONGODB_SERVER
        self.port = settings.MONGODB_PORT
        self.db = settings.MONGODB_DB
        self.col = settings.MONGODB_COLLECTION
        # connection = pymongo.Connection(self.server, self.port)
        self.client = pymongo.MongoClient(self.server, self.port)

    def insert(self, json):
        col = self.client.get_database(self.db).get_collection(self.col)
        col.insert_one(eval(json))
