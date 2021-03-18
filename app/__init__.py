from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def page_not_found(error):
    return render_template('errors/404.html')


def initializer(config):
    app.config.from_object(config)
    app.register_error_handler(404, page_not_found)
    return app
