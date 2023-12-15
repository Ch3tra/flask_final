from flask import Blueprint, render_template

from config import execute_query

poss = Blueprint('poss', __name__)


@poss.route('/admin/pos')
def pos():
    return render_template('admin/pos.html')
