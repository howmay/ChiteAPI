from pymongo import collection
from chite.application import mongo


class MongoDB(object):
    @staticmethod
    def Insert(collection: str, data) -> bool:
        c = _get_collection(collection)
        _id = c.insert_one(data).inserted_id
        if _id is not None:
            return True
        return False

    @staticmethod
    def InsertMany(collection: str, data):
        pass


def _get_collection(collection: str) -> collection:
    if collection == "product":
        return mongo.db.product
    elif collection == "material":
        return mongo.db.material
