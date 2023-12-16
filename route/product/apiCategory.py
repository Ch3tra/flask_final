from flask import Blueprint, jsonify
from flask_login import login_required

from config import execute_query

apiC = Blueprint('apiC', __name__)


@apiC.route('/getAllCategory')
@login_required
def getAllCategory():
    query = "SELECT * FROM category"
    categories = execute_query(query)

    json_string = []
    for category in categories:
        json_string.append(
            {
                'id': category['categoryId'],
                'name': category['categoryName'],
                'desc': category['categoryDesc'],
            }
        )
    return jsonify(cate=json_string)

