from flask import Blueprint, jsonify, request
from flask_login import login_required

from config import execute_query

apiC = Blueprint('apiC', __name__)


@apiC.route('/getAllCategory')
@login_required
def getAllCategory():
    query = "SELECT * FROM category ORDER BY categoryId DESC"
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


@apiC.route('/admin/category_added', methods=['POST'])
@login_required
def category_added():
    try:
        name = request.form['name']
        description = request.form['desc']

        query = "INSERT INTO category (categoryName, categoryDesc) VALUES (%s, %s)"
        params = (name, description)

        execute_query(query, params, is_insert=True)

        return jsonify({'message': 'Category added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@apiC.route('/admin/category_edit', methods=['POST'])
@login_required
def category_edit():
    try:
        pid = request.form['id']
        name = request.form['name']
        description = request.form['desc']

        query = f"UPDATE category SET " \
                f"categoryName = %s, " \
                f"categoryDesc = %s " \
                f"WHERE categoryId = %s"
        params = (name, description, pid)

        execute_query(query, params, is_insert=True)

        return jsonify({'message': 'Category edited successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@apiC.route('/admin/category_delete', methods=['POST'])
@login_required
def category_delete():
    try:
        cid = request.form['id']

        query = f"DELETE FROM category WHERE categoryId = %s"
        execute_query(query, (cid,), is_insert=True)

        return jsonify({'message': 'Category deleted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500