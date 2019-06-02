import pymongo
class MongoDB(object):
    URI = 'mongodb://127.0.0.1:27017'
    @staticmethod
    def init():
        client = pymongo.MongoClient(MongoDB.URI)
        MongoDB.DATABASE = client['Chite']
    @staticmethod
    def Insert(collection: str, data) -> bool:
        MongoDB.DATABASE[collection].insert(data)
        return True
