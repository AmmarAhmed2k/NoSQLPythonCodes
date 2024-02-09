# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 02:56:44 2023
@author: Ammar Ahmed Siddiqui
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ammarahmed2k:pakistan5040@cluster0.hycem2f.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    exit()

# select the 'training' database 
db = client.training


# create a sample document
doc = {"lab":"Accessing mongodb using python", "Subject":"No SQL Databases"}

# insert a sample document

for x in range(1 , 50):   
    print("Inserting a document into collection.")
    doc = {"lab":"Accessing mongodb using python", "Subject":"No SQL Databases", "Number":x}
    print(db.AmmarCollection.insert_one(doc))
    print(doc)

# query for all documents in 'training' database and 'AmmarCollection' collection
docs = db.AmmarCollection.find()

print("Printing the documents in the collection.")
for document in docs:
    print(document)

# close the server connecton
print("Closing the connection.")
client.close()
