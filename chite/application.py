# -*- coding: utf-8 -*-

#from config import Config

from flask import Flask, render_template
from flask_pymongo import PyMongo

import os

mongo = PyMongo()


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.config["APPLICATION_ROOT"] = "/api"

    mongo.init_app(app)

    from .product import Product as product_blueprint
    app.register_blueprint(product_blueprint)

    from .material import Material as material_blueprint
    app.register_blueprint(material_blueprint)

    app.config['SECRET_KEY'] = os.urandom(24)

    # from .middleware import Middleware
    # app.wsgi_app = Middleware(app.wsgi_app)

    return app
