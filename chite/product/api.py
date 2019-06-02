# -*- coding: utf-8 -*-

from . import Product
from flask import jsonify, request, session, logging, abort
from bson import json_util
from chite.model import ProductModel


@Product.route('/product', methods=['GET'])
def GetProduct():
    return jsonify({}), 200


@Product.route('/product', methods=['POST'])
def PostProduct():
    data = request.json
    print(data)
    return jsonify({}), 200


@Product.route('/product', methods=['PUT'])
def PutProduct():
    return jsonify({}), 200


@Product.route('/product', methods=['DELETE'])
def DeleteProduct():
    return jsonify({}), 200


# {
#     "_id":"9001401801"
# 	  "material": "MDF",
#     "images": ["http://www.google.com/1.jpg"],
#     "productName": "White-客供色版",
#     "specificatio": ["800*480*15MM","800*115*15MM"],
#     "unreportedTax": 85.0,
#     "accessories_list": [{
#     	"images": ["http://www.google.com/1.jpg"],
# 	    "ai_id": "A",
# 	    "accessoriesName": "平面內六角",
# 	    "specification": ["M6*28MM 黑色","生產改為, M6*30MM"],
# 	    "set_num": 6,
# 	    "unit": "PCS"
#     }]
# }
