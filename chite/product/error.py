from . import Product
from flask import jsonify, logging


@Product.app_errorhandler(400)
def handle_bad_request(e):
    logging.logging.warn('Bad requets. about :%s' % (e.description))
    return jsonify({
        'Message': "error"
    }), 400


@Product.app_errorhandler(404)
def handle_not_found(e):
    return jsonify({
        'Message': e
    }), 404


@Product.app_errorhandler(Exception)
def handle_server_error(e):
    logging.logging.error("server error. about :%s" % (e.description))
    return jsonify({
        'Message': e
    }), 500
