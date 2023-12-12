from flask import Blueprint, render_template

products = Blueprint('products', __name__)


@products.route('/admin/product')
def product():
    return render_template('admin/product/product_list.html')

