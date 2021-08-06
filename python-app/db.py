from mongo import MongoConnection
import requests
from flask import Flask ,jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import csv
app = Flask(__name__)
api = Api(app)
host='mongodb'
port=27017
dbname='mahmoud_db'
dbcollection='new_collection'
mongoConnection=MongoConnection(host,port)

###################################################
class Vehicles(Resource):
    def get(self):
        retrieved_data=mongoConnection.retrieveData(dbname,dbcollection)
        return {'data': retrieved_data}, 200  # return data and 200 OK code
    

############################################################
api.add_resource(Vehicles, '/vehicles')  # '/vehicles' is our entry point for Users




if __name__ == '__main__':
    app.run(host='ns3160817.ovh.net',port=5005)  # run our Flask app