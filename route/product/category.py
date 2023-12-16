from flask import Blueprint, render_template
from flask_login import login_required

categories = Blueprint('categories', __name__)


@categories.route('/admin/category')
@login_required
def category():
    return render_template('admin/product/category_list.html')