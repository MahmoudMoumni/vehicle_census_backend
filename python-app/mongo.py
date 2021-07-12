import pymongo 

class MongoConnection:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.mongo_connection=pymongo.MongoClient(host,port)

    def insertData(self,dbname,dbcollection,data):
        mydb =self.mongo_connection[dbname]
        mycollection = mydb[dbcollection]
        mycollection.insert_many(data)

    def retrieveData(self,dbname,dbcollection):
        mydb =self.mongo_connection[dbname]
        mycollection = mydb[dbcollection]
        cursor = mycollection.find()
        entries = list(cursor)
        return entries

        