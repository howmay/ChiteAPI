# -*- coding: utf-8 -*-

from . import Material
from flask import jsonify, request, session, logging
from chite.store import MongoDB
from bson import json_util


@Material.route('/material', methods=['GET'])
def GetProduct():
    return '', 200


@Material.route('/material', methods=['POST'])
def PostProduct():
    return '', 200


@Material.route('/material', methods=['PUT'])
def PutProduct():
    return '', 200


@Material.route('/material', methods=['DELETE'])
def DeleteProduct():
    return '', 200
