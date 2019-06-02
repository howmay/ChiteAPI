from .application import mongo
from datetime import datetime


class Test(mongo.Document):
    _id = mongo.StringField()
    test = mongo.StringField()


class ProductModel(mongo.Document):
    _id = mongo.StringField()
    material = mongo.StringField()
    images = mongo.ListField()
    productName = mongo.StringField()
    specification = mongo.ListField()
    unreportedTax = mongo.FloatField()
    creation_date = mongo.DateTimeField()
    modified_date = mongo.DateTimeField(default=datetime.now)
