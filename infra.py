from flask import Flask
import json
import bcrypt
import pymongo

# Connect to the data base
########################################

try:
    mongo = pymongo.MongoClient(
        "127.0.0.1",
        port=27017,
        serverSelectionTimeOutMS=1000)
    db = mongo.test
    print("que hay aqui:  " + str(db))
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
            print("Login error: mail or password invalid")
            return False
        else:
            print("User loged")
            return True

    except Exception as ex:
        pass
    return "Ok"
