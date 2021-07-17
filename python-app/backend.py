# Import Module
import os
import csv
from mongo import MongoConnection

import os
cwd=os.getcwd()
print(cwd)

# Folder Path
path = "./data"

#mongo config
host='mongodb'#service name
port=27017#internal port
dbname='mahmoud_db'
dbcollection='new_collection'
mongoConnection=MongoConnection(host,port)  

  
  
def read_text_file(file_path):
    csv_data=[]
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader, None)
        if headers is None:
            return 
        print(headers)
        lg_headers=len(headers)
        for row in reader:
            cur_data={}
            for i in range(lg_headers):
                cur_data[headers[i]]=row[i]
            print(cur_data)
            csv_data.append(cur_data)
            
    
    print("INSERTING DATA")
    #print(csv_data)
    if len(csv_data):
        
        return 
        mongoConnection.insertData(dbname,dbcollection,csv_data)
  
  
def scan_folder(path):
    # iterate through all file
    for file in os.listdir(path):
    # Check whether file is in text format or not
        if file.endswith(".csv"):
            file_path = path+"/"+file
            print("file name: "+file_path)
            # call read text file function
            read_text_file(file_path)

scan_folder(path)
