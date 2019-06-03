# -*- coding: utf-8 -*-

from . import General
from flask import jsonify, request, session, logging


@General.route('/ping')
def GetProduct():
    return 'pong', 200
