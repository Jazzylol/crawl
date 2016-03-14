import pymongo


class MongoHelper(object):
	def __init__(self):
		# self.server = settings['MONGODB_SERVER']
		# self.port = settings['MONGODB_PORT']
		# self.db = settings['MONGODB_DB']
		# self.col = settings['MONGODB_COLLECTION']
		self.server = "191.168.1.156"
		self.port = 27017
		self.db = "crawl"
		self.col = "meituan"
		# connection = pymongo.Connection(self.server, self.port)
		client = pymongo.MongoClient("192.168.1.156", 27017)
		db = client['crawl']
		collection = db['meituan']
		su = collection.insert({"a": "b"})
		print su


m = MongoHelper()
