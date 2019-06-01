# -*- coding: utf-8 -*-

from . import Product
from flask import jsonify, request, session, logging
from chite.store import MongoDB
from bson import json_util


@Product.route('/product', methods=['GET'])
def GetProduct():
    return '', 200


@Product.route('/product', methods=['POST'])
def PostProduct():
    return '', 200


@Product.route('/product', methods=['PUT'])
def PutProduct():
    return '', 200


@Product.route('/product', methods=['DELETE'])
def DeleteProduct():
    return '', 200
