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
databases = connect_mongodb (db_username='freda', db_passw='', db_name='mydb')
#generate my clusters
my_cluster = databases.mobile_numbers


#create query as dict variable 
query1 = {"Adress" : "Tirane"}
query2 = {"HasPhone" : 0}
query3 = {"HasEmail": 1 }


#generate the cluster with the query conditions
#cluster is a cursor so convert it as a list to check if it is empty
y = list(my_cluster.find(query1))
if len(y) == 0:
    print("Theres no data with the Tirane adress")
else:
    print("There are",len(y)," data with Tirane adress")
    #print("This data are:")
    #for x in y:
        #print(x)

#print only the value of the key that satisfy query3
for mail in my_cluster.find(query3):
      print(mail["Email"])
      
#the phone numbers of tirana adress    
for phones in my_cluster.find(query1):
      print(phones["Phone"])
