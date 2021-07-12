from mongo import MongoConnection
import requests

host='mongodb'
port=27017
dbname='mahmoud_db'
dbcollection='new_collection'
mongoConnection=MongoConnection(host,port)
#data=
#mongoConnection.insertData(dbname,dbcollection,data)

retrieved_data=mongoConnection.retrieveData(dbname,dbcollection)
print("data retrieved")
print(retrieved_data)

