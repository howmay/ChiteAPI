from . import Material
from flask import jsonify, logging


@Material.app_errorhandler(400)
def handle_bad_request(e):
    logging.logging.warn('Bad requets. about :%s' % (e.description))
    return jsonify({
        'Message': "error"
    }), 400


@Material.app_errorhandler(404)
def handle_not_found(e):
    return jsonify({
        'Message': e
    }), 404


@Material.app_errorhandler(Exception)
def handle_server_error(e):
    logging.logging.error("server error. about :%s" % (e.description))
    return jsonify({
        'Message': e
    }), 500
