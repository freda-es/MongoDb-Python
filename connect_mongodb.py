import urllib
import certifi
from pymongo import MongoClient
from unicodedata import name

#connect mongodb
def connect_mongodb (db_username, db_passw, db_name):
    MONGODB_USERNAME = urllib.parse.quote_plus(db_username)
    MONGODB_PASSWORD = urllib.parse.quote_plus(db_passw)
    MONGODB_DATABASE = db_name
    ca = certifi.where()
    MONGODB_URL = "mongodb+srv://"+MONGODB_USERNAME+":"+MONGODB_PASSWORD+"@cluster0.ks8wq.mongodb.net/"+MONGODB_DATABASE+"?retryWrites=true&w=majority"
    client = MongoClient(MONGODB_URL, tlsCAFile=ca)
    database = client.get_database(db_name)
    return database
#call the function to generate your own db
databases = connect_mongodb (db_username='', db_passw='', db_name='dbECommerce')
#generate cluster
my_cluster = databases.users
