import urllib
import certifi
import json
import pandas as pd
import pymongo
from unicodedata import name

#connect to mongodb
def connect_mongodb (db_username, db_passw, db_name):
    MONGODB_USERNAME = urllib.parse.quote_plus(db_username)
    MONGODB_PASSWORD = urllib.parse.quote_plus(db_passw)
    MONGODB_DATABASE = db_name
    ca = certifi.where()
    MONGODB_URL = "mongodb+srv://"+MONGODB_USERNAME+":"+MONGODB_PASSWORD+"@cluster0.ks8wq.mongodb.net/"+MONGODB_DATABASE+"?retryWrites=true&w=majority"
    client = pymongo.MongoClient(MONGODB_URL, tlsCAFile=ca)
    return client

#function to import a csv file, with a new dbname and new collection name
def mongoimport(csv_path, db_name, coll_name):
    db = databases[db_name]
    coll = db[coll_name]
    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))
    coll.insert_many(payload)
    return coll


databases = connect_mongodb (db_username='', db_passw='', db_name='dbECommerce')
mongoimport(csv_path="C:\\Users\\..\\Code\\python\\e-commerce\\MyData.csv", db_name="mydb", coll_name="mobile_numbers")
