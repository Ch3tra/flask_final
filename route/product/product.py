from flask import Blueprint, render_template
from flask_login import login_required

products = Blueprint('products', __name__)


@products.route('/admin/product')
@login_required
def product():
    return render_template('admin/product/main_product.html')

