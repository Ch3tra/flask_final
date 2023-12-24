from flask import Blueprint, render_template
from flask_login import login_required

students = Blueprint('students', __name__)


@students.route('/admin/student')
@login_required
def student():
    return render_template('admin/student/main_student.html')