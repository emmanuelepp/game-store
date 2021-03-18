from flask import Flask, render_template, request

app = Flask(__name__)

data = {
    'title': 'Index',
    'header': 'welcome'
}


@app.route('/')
def index():
    return render_template('index.html', data=data)


@app.route('/contact')
def contact():
    data = {
        'title': 'Contact',
        'header': 'welcome'
    }
    return render_template('contact.html', data=data)


@app.route('/data')
def data():
    value = request.args.get('value')
    return 'This are the values:  {0}'.format(value)


if __name__ == '__main__':
    app.run(debug=True)
