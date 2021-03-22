from flask import Flask, request, redirect, url_for, render_template
from flask_wtf.csrf import CSRFProtect
import datetime
import infra
import pymongo


app = Flask(__name__)

csrf = CSRFProtect()

infra = infra


@app.route('/login', methods=['GET', 'POST'])
def login():
    date = datetime.datetime.now().strftime('%Y')
    if request.method == 'POST':
        user_validation = infra.validate_user(
            request.form['user'], request.form['password'])
        if user_validation == True:
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html', date=date)
    else:
        return render_template('auth/login.html', date=date)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_user', methods=['POST'])
def add_user(user, password):
    infra.create_user(user, password)

    return 'Ok'


def page_not_found(error):
    return render_template('errors/404.html')


def initializer(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, page_not_found)
    return app
