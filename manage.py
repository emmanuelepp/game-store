from flask_script import Manager
from app import initializer
from config import config

configuration = config['development']
app = initializer(configuration)

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
