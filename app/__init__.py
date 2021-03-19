from flask import Flask, request, redirect, url_for, render_template
from flask_wtf.csrf import CSRFProtect
import datetime


app = Flask(__name__)

csrf = CSRFProtect()

# CSRF protection


@app.route('/login', methods=['GET', 'POST'])
def login():
    date = datetime.datetime.now().strftime('%Y')
    if request.method == 'POST':
        if request.form['user'] == 'admin' and request.form['password'] == '123456':
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html', date=date)


@app.route('/')
def index():
    return render_template('index.html')


def page_not_found(error):
    return render_template('errors/404.html')


def initializer(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, page_not_found)
    return app
