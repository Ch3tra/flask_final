from flask import Flask, render_template

from route.product.apiCategory import apiC
from route.product.apiProduct import apiD
from route.product.category import categories
from route.product.product import products

app = Flask(__name__)


app.register_blueprint(products)
app.register_blueprint(categories)
app.register_blueprint(apiD)
app.register_blueprint(apiC)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('admin/index.html')


if __name__ == '__main__':
    app.run()


