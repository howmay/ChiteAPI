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
