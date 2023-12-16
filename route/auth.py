from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from config import execute_query


auths = Blueprint('auths', __name__)
login_manager = LoginManager()


class User(UserMixin):
    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash

    def get(user_id):
        query = f"SELECT * FROM credential WHERE userId = %s"
        user_data = execute_query(query, (user_id,))
        if user_data:
            return User(user_data[0]['userId'], user_data[0]['username'], user_data[0]['password_hash'])

    def get_by_username(username):
        query = f"SELECT * FROM credential WHERE username = %s"
        user_data = execute_query(query, (username,))
        if user_data:
            return User(user_data[0]['userId'], user_data[0]['username'], user_data[0]['password_hash'])

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


# ** register new admin user
@auths.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Hash the password
        password_hash = generate_password_hash(password)

        # Insert the new user into the database
        sql = "INSERT INTO credential (username, password_hash) VALUES (%s, %s)"
        execute_query(sql, (username, password_hash), "ss34_proo", True)

        return redirect(url_for('admin'))
    return render_template('admin/register.html')


# ** login
@auths.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.get_by_username(username)
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('auths.protected'))
    return render_template('admin/login.html')


@auths.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('admin/login.html')


@auths.route('/protected')
@login_required
def protected():
    return render_template('admin/index.html')
