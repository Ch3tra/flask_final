import os

from flask import Blueprint, jsonify, request, current_app
from flask_login import login_required
from werkzeug.utils import secure_filename

from config import execute_query

apiS = Blueprint('apiS', __name__)


@apiS.route('/getAllStudent')
@login_required
def getAllStudent():
    query = "SELECT * FROM STUDENT ORDER BY sid DESC"
    students = execute_query(query)

    json_string = []

    for student in students:
        json_string.append(
            {
                'id': student['sid'],
                'firstName': student['firstName'],
                'lastName': student['lastName'],
                'birthday': student['birthday'],
                'gender': student['gender'],
                'email': student['email'],
                'phoneNumber': student['phoneNumber'],
                'subject': student['subject'],
                'image': student['image'],
            }
        )

    return jsonify(students=json_string)


@apiS.route('/admin/student_added', methods=['POST'])
@login_required
def student_added():
    try:
        fname = request.form['firstName']
        lname = request.form['lastName']
        gender = request.form['gender']
        birthday = request.form['birthday']
        email = request.form['email']
        phone = request.form['phone']
        subject = request.form['subject']
        image = request.files.get('image_upload')

        if image:
            _, extension = os.path.splitext(image.filename)
            if extension.lower() not in ['.jpg', '.png', '.jfif']:
                return 'Invalid file type. Only jpg, png, and jfif files are allowed.', 400

            file_size = image.content_length  # Get file size directly from the request

            if file_size > 2 * 1024 * 1024:  # 2MB limit
                return 'File size is too large. The maximum file size is 2MB.', 400

            filename = secure_filename(f"{fname}{lname}{extension}")
            image.save(os.path.join(current_app.config['UPLOAD_FOLDER_STUDENT'], filename))

            query = "INSERT INTO student (firstName, lastName, birthday, gender, email, phoneNumber, subject, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            params = (fname, lname, birthday, gender, email, phone, subject, filename)
        else:
            query = "INSERT INTO student (firstName, lastName, birthday, gender, email, phoneNumber, subject) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            params = (fname, lname, birthday, gender, email, phone, subject)

        execute_query(query, params, is_insert=True)

        return jsonify({'message': 'Student added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@apiS.route('/admin/student_edited', methods=['POST'])
@login_required
def student_edited():
    try:
        sid = request.form['id']
        fname = request.form['firstName']
        lname = request.form['lastName']
        gender = request.form['gender']
        birthday = request.form['birthday']
        email = request.form['email']
        phone = request.form['phone']
        subject = request.form['subject']
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
            old_image_query = "SELECT image FROM student WHERE sid = %s"
            old_image_filename = execute_query(old_image_query, (sid,), is_insert=False)[0]['image']

            # Delete the old image file
            if old_image_filename:
                old_image_path = os.path.join(current_app.config['UPLOAD_FOLDER_STUDENT'], old_image_filename)
                if os.path.isfile(old_image_path):
                    os.remove(old_image_path)

            # Save the image to the upload folder, with name.extension as the filename
            filename = secure_filename(f"{fname}{lname}{extension}")
            image.save(os.path.join(current_app.config['UPLOAD_FOLDER_STUDENT'], filename))

            query = f"UPDATE student SET " \
                    f"firstName = %s, " \
                    f"lastName = %s, " \
                    f"gender = %s, " \
                    f"birthday = %s, " \
                    f"email = %s, " \
                    f"phoneNumber = %s, " \
                    f"subject = %s, " \
                    f"image = %s " \
                    f"WHERE sid = %s"
            params = (fname, lname, gender, birthday, email, phone, subject, filename, sid)
        else:
            query = f"UPDATE student SET " \
                    f"firstName = %s, " \
                    f"lastName = %s, " \
                    f"gender = %s, " \
                    f"birthday = %s, " \
                    f"email = %s, " \
                    f"phoneNumber = %s, " \
                    f"subject = %s " \
                    f"WHERE sid = %s"
            params = (fname, lname, gender, birthday, email, phone, subject, sid)

        execute_query(query, params, is_insert=True)

        return jsonify({'message': 'Student edited successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@apiS.route('/admin/student_delete', methods=['POST'])
@login_required
def student_delete():
    try:
        id = request.form['id']
        image = request.form['image']

        # check if image not default image
        if image != 'default_img':
            image_path = os.path.join(current_app.config['UPLOAD_FOLDER_STUDENT'], image)
            if os.path.isfile(image_path):
                os.remove(image_path)

        query = f"DELETE FROM student WHERE sid = %s"
        execute_query(query, (id,), is_insert=True)

        return jsonify({'message': 'Student deleted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500