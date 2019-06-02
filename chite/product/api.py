# -*- coding: utf-8 -*-

from . import Product
from flask import jsonify, request, session, logging, abort
from bson import json_util
from chite.model import Product


@Product.route('/product', methods=['GET'])
def GetProduct():
    return jsonify({}), 200


@Product.route('/product', methods=['POST'])
def PostProduct():
    return jsonify({}), 200


@Product.route('/product', methods=['PUT'])
def PutProduct():
    return jsonify({}), 200


@Product.route('/product', methods=['DELETE'])
def DeleteProduct():
    return jsonify({}), 200
