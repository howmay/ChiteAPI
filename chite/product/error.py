from . import Product
from flask import jsonify, logging


@Product.app_errorhandler(400)
def handle_bad_request(e):
    logging.logging.warn('Bad requets. about ')
    return jsonify({
        'Message': ''
    }), 400


@Product.app_errorhandler(404)
def handle_not_found(e):
    return jsonify({
        'Message': ''
    }), 404


@Product.app_errorhandler(Exception)
def handle_server_error(e):
    logging.logging.error("server error. about")
    return jsonify({
        'Message': ''
    }), 500
