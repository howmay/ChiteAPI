from flask import Blueprint
Product = Blueprint('Product',__name__)

from . import api
from . import error
