import os

from flask import Blueprint, jsonify, request, current_app
from flask_login import login_required
from werkzeug.utils import secure_filename

from config import execute_query

apiD = Blueprint('apiD', __name__)


@apiD.route('/getAllProduct')
def getAllProduct():
    query = "SELECT product.*, category.categoryName AS category_name FROM product LEFT JOIN category ON product.categoryId = category.categoryId"
    products = execute_query(query)

    query = "SELECT categoryId, categoryName from category"
    categories = execute_query(query)

    json_string = []
    json_string_category = []

    for product in products:
        json_string.append(
            {
                'id': product['productId'],
                'name': product['productName'],
                'category': product['category_name'],
                'desc': product['productDesc'],
                'cost': product['productCost'],
                'image': product['image'],
            }
        )
    for category in categories:
        json_string_category.append(
            {
                'id': category['categoryId'],
                'name': category['categoryName'],
            }
        )
    return jsonify(products=json_string, categories=json_string_category)


@apiD.route('/admin/product_added', methods=['POST'])
def product_added():
    try:
        name = request.form['name']
        description = request.form['description']
        cost = request.form['cost']
        category = request.form['category']

        image = request.files.get('image_upload')

        if image:
            _, extension = os.path.splitext(image.filename)
            if extension.lower() not in ['.jpg', '.png', '.jfif']:
                return 'Invalid file type. Only jpg, png, and jfif files are allowed.', 400

            if image.content_length > 2 * 1024 * 1024:  # 2MB limit
                return 'File size is too large. The maximum file size is 2MB.', 400

            filename = secure_filename(f"{name}{extension}")
            image.save(os.path.join(current_app.config['UPLOAD_FOLDER_PRODUCT'], filename))

            query = "INSERT INTO product (productName, productDesc, productCost, categoryId, image) VALUES (%s, %s, %s, %s, %s)"
            params = (name, description, cost, category, filename)
        else:
            query = "INSERT INTO product (productName, productDesc, productCost, categoryId) VALUES (%s, %s, %s, %s)"
            params = (name, description, cost, category)

        execute_query(query, params, is_insert=True)

        return jsonify({'message': 'Product added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

