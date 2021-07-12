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
        for row in reader:
            cur_data={
                'x1':row[0],
                'x2':row[1],
                'x3':row[2],
                'x4':row[3],
                'x5':row[4],
                'x6':row[5],
                'x7':row[6],
                'x8':row[7],
                'x9':row[8],
                'x10':row[9]
            }
            csv_data.append(cur_data)
            break
    
    print("INSERTING DATA")
    #print(csv_data)
    if len(csv_data):
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
