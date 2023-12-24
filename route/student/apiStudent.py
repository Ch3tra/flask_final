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