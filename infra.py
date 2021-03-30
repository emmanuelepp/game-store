from flask import Flask
import json
import bcrypt
import pymongo
import logging

# Connect to the data base
########################################
logging.basicConfig(filename='./logs/app.log',
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

try:
    mongo = pymongo.MongoClient(
        "127.0.0.1",
        port=27017,
        serverSelectionTimeOutMS=1000)
    db = mongo.test

    mongo.server_info()
except Exception as ex:
    print("Error: " + ex)
    pass


# Core methods
########################################
def create_user(userName, password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

    try:
        user = {
            'user': userName,
            'password': hashed
        }

        mongo.test.user.insert(user)

    except Exception as ex:
        pass
    return "Ok"


def validate_user(user, password):

    salt = bcrypt.gensalt()

    try:
        response = mongo.test.user.find_one({'user': user})
        print(response)

        res = response.get('password')
        unhashed = bcrypt.checkpw(password.encode('utf-8'), res)

        if unhashed is not True:
            logging.info("Login error: mail or password invalid")
            return False
        else:
            logging.info("User loged")
            return True

    except Exception as ex:
        logging.info("Error: User not loged")

    return "Ok"


def get_user_by_id(user):
    # try:
    #     reponse = mongo.test.user.find_one({'user': user})

    #     return reponse.get('user')

    # except Exception as ex:
    # return "Ok"
    pass
