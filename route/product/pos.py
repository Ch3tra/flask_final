from flask import Blueprint, render_template
from flask_login import login_required

poss = Blueprint('poss', __name__)


@poss.route('/admin/pos')
@login_required
def pos():
    return render_template('admin/pos.html')
