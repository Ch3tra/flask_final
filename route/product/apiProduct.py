from flask import Blueprint, jsonify
from flask_login import login_required

from config import execute_query

apiD = Blueprint('apiD', __name__)


@apiD.route('/getAllProduct')
def getAllProduct():
    query = "SELECT product.*, category.categoryName AS category_name FROM product LEFT JOIN category ON product.categoryId = category.categoryId"
    products = execute_query(query)

    json_string = []
    for product in products:
        json_string.append(
            {
                'id': product['productId'],
                'name': product['productName'],
                'category': product['category_name'],
                'desc': product['productDesc'],
                'price': product['productPrice'],
                'image': product['image'],
            }
        )
    return jsonify(products=json_string)



