from flask import Flask, render_template
from flask_login import login_required

from route.apiFProduct import apiFD
from route.auth import auths, login_manager
from route.product.apiCategory import apiC
from route.product.apiProduct import apiD
from route.product.category import categories
from route.product.pos import poss
from route.product.product import products

app = Flask(__name__)


app.secret_key = 'ohboitakeiteasyss'  # Change this!

login_manager.init_app(app)
login_manager.login_view = "auths.login"


app.config['UPLOAD_FOLDER_PRODUCT'] = 'static/img/product'

app.register_blueprint(products)
app.register_blueprint(categories)
app.register_blueprint(apiD)
app.register_blueprint(apiC)
app.register_blueprint(apiFD)
app.register_blueprint(poss)
app.register_blueprint(auths, url_prefix='/auth')


@app.route('/')
def index():
    return render_template('frontend/index.html')


@app.route('/admin')
@login_required
def admin():
    return render_template('admin/index.html')


# ** handling 404
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error/404.html'), 404


# ** handling 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error/500.html'), 500

if __name__ == '__main__':
    app.run()


