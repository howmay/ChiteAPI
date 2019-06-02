from datetime import datetime
from chite.application import MongoDB
from flask import jsonify

class Test(object):
    def __init__(self,title,content,createTime):
        self.title = title
        self.content = content
        self.createTime = createTime
    def insert(self):
        MongoDB.Insert(collection='Test',data=self.json())
    def json(self):
        return {
            'title': self.title,
            'content': self.content,
            'createTime' : self.createTime
        }
# class ProductModel(mongo.Document):
#     _id = mongo.StringField()
#     material = mongo.StringField()
#     images = mongo.ListField()
#     productName = mongo.StringField()
#     specification = mongo.ListField()
#     unreportedTax = mongo.FloatField()
#     creation_date = mongo.DateTimeField()
#     modified_date = mongo.DateTimeField(default=datetime.now)
