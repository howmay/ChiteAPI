# -*- coding: utf-8 -*-

#from config import Config

from flask import Flask, render_template
from chite.store import MongoDB
import os

def create_app(config):
    app = Flask(__name__)
    MongoDB.init()
    from .product import Product as product_blueprint
    app.register_blueprint(product_blueprint)

    from .material import Material as material_blueprint
    app.register_blueprint(material_blueprint)
    return app
