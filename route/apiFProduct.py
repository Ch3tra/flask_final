from flask import Blueprint, request, jsonify

from config import execute_query

apiFD = Blueprint('apiFD', __name__)


@apiFD.route('/getAllFProduct')
def getAllFProduct():
    filter_category = request.args.get('filter_category', default='all', type=str)

    queryCate = """
        SELECT * FROM category
    """
    categories = execute_query(queryCate)

    query = """
        SELECT p.productId, p.productName, p.productPrice, c.categoryName AS category
        FROM product p
        JOIN category c ON p.categoryId = c.categoryId
    """

    if filter_category != 'all':
        query += " WHERE c.categoryName = %s"
        products = execute_query(query, (filter_category,))
    else:
        products = execute_query(query)

    json_data = []
    json_data_cate = []

    for product in products:
        json_data.append({
            'id': product['productId'],
            'name': product['productName'],
            'price': product['productPrice'],
            'category': product['category']
        })

    for category in categories:
        json_data_cate.append({
            'id': category['categoryId'],
            'name': category['categoryName'],
        })

    return jsonify(products=json_data, categories=json_data_cate)
