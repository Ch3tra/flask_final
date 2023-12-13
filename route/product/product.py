import os

from flask import Blueprint, render_template, request, jsonify, app
from werkzeug.utils import secure_filename

from config import execute_query

products = Blueprint('products', __name__)


@products.route('/admin/product')
def product():
    return render_template('admin/product/product_list.html')

