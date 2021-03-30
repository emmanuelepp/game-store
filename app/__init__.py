from flask import Flask, request, redirect, url_for, render_template
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user
import datetime
import infra
import pymongo


app = Flask(__name__)

csrf = CSRFProtect()

infra = infra
#login_manager_app = LoginManager(app)


@app.route('/login', methods=['POST', 'GET'])
def login():
    date = datetime.datetime.now().strftime('%Y')
    if request.method == 'POST':
        user_validation = infra.validate_user(
            request.form['user'], request.form['password'])
        if user_validation == True:
            # login_user(infra.get_user_by_id(request.form['user']))
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html', date=date)
    else:
        return render_template('auth/login.html', date=date)


@app.route('/logout')
def logout():
    # logout_user()
    return redirect(url_for('login'))


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    infra.create_user("Emmanuel", "Ponciponci")

    return 'Ok'


def page_not_found(error):
    return render_template('errors/404.html')


def initializer(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, page_not_found)
    return app
