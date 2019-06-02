from .application import mongo
from datetime import datetime


class ProductModel():
    _id = ""
    material = ""
    images = []
    productName = ""
    specification = []
    unreportedTax = mongo.FloatField()
    creation_date = mongo.DateTimeField()
    modified_date = mongo.DateTimeField(default=datetime.now)
