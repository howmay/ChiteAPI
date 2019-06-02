from .application import mongo
from datetime import datetime
from typing import List


class ProductModel(object):
    _id: str
    material: str
    images: list
    productName: str
    specification: list
    unreportedTax: float
    accessories_list: list
    creation_date: datetime
    modified_date: datetime

    def __init__(self):
        self.modified_date = datetime.now()
        pass


class AccessoriesModel(object):
    _id: str
    images: list
    ai_id: str
    accessoriesName: str
    specification: list
    set_num: int
    unit: str
