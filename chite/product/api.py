# -*- coding: utf-8 -*-

from . import Product
from flask import jsonify, request, session, logging, abort
from bson import json_util
from chite.model import ProductModel, Test


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


@Product.route('/test', methods=["GET"])
def test():
    Test().save()
    data = Test.objects.all()
    return jsonify(data), 200
