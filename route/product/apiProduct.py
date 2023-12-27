import os

from flask import Blueprint, jsonify, request, current_app
from flask_login import login_required
from werkzeug.utils import secure_filename

from config import execute_query

apiD = Blueprint('apiD', __name__)


@apiD.route('/getAllProduct')
@login_required
def getAllProduct():
    query = "SELECT product.*, category.categoryName AS category_name FROM product LEFT JOIN category ON product.categoryId = category.categoryId ORDER BY product.productId DESC"
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
                'discount': product['discount'],
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
@login_required
def product_added():
    try:
        name = request.form['name']
        description = request.form['desc']
        cost = request.form['cost']
        category = request.form['category']

        image = request.files.get('image_upload')

        if image:
            _, extension = os.path.splitext(image.filename)
            if extension.lower() not in ['.jpg', '.png', '.jfif']:
                return 'Invalid file type. Only jpg, png, and jfif files are allowed.', 400

            file_size = image.content_length  # Get file size directly from the request

            if file_size > 2 * 1024 * 1024:  # 2MB limit
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


@apiD.route('/admin/product_edit', methods=['POST'])
@login_required
def product_edit():
    try:
        pid = request.form['id']
        name = request.form['name']
        description = request.form['desc']
        cost = request.form['cost']
        category = request.form['category']

        image = request.files.get('image_upload')

        # check if user input image or not
        if image:
            # Check the file extension
            _, extension = os.path.splitext(image.filename)
            if extension.lower() not in ['.jpg', '.png', '.jfif']:
                return 'Invalid file type. Only jpg, png, and jfif files are allowed.', 400

            # Check the file size (2MB = 2 * 1024 * 1024 bytes)
            if image.content_length > 2 * 1024 * 1024:
                return 'File size is too large. The maximum file size is 2MB.', 400

            # Get the old image filename from the database
            old_image_query = "SELECT image FROM product WHERE productId = %s"
            old_image_filename = execute_query(old_image_query, (pid,), is_insert=False)[0]['image']

            # Delete the old image file
            if old_image_filename:
                old_image_path = os.path.join(current_app.config['UPLOAD_FOLDER_PRODUCT'], old_image_filename)
                if os.path.isfile(old_image_path):
                    os.remove(old_image_path)

            # Save the image to the upload folder, with name.extension as the filename
            filename = secure_filename(f"{name}{extension}")
            image.save(os.path.join(current_app.config['UPLOAD_FOLDER_PRODUCT'], filename))

            query = f"UPDATE product SET " \
                    f"categoryId = %s, " \
                    f"productName = %s, " \
                    f"productDesc = %s, " \
                    f"productCost = %s, " \
                    f"image = %s " \
                    f"WHERE productId = %s"
            params = (category, name, description, cost, filename, pid)
        else:
            query = f"UPDATE product SET " \
                    f"categoryId = %s, " \
                    f"productName = %s, " \
                    f"productDesc = %s, " \
                    f"productCost = %s " \
                    f"WHERE productId = %s"
            params = (category, name, description, cost, pid)

        execute_query(query, params, is_insert=True)

        return jsonify({'message': 'Product edited successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@apiD.route('/admin/product_delete', methods=['POST'])
@login_required
def product_delete():
    try:
        pid = request.form['id']
        image = request.form['image']

        # check if image not default image
        if image != 'default_img':
            image_path = os.path.join(current_app.config['UPLOAD_FOLDER_PRODUCT'], image)
            if os.path.isfile(image_path):
                os.remove(image_path)

        query = f"DELETE FROM product WHERE productId = %s"
        execute_query(query, (pid,), is_insert=True)

        return jsonify({'message': 'Product deleted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
