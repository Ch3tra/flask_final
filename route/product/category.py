from flask import Blueprint, render_template

categories = Blueprint('categories', __name__)


@categories.route('/admin/category')
def category():
    return render_template('admin/product/category_list.html')