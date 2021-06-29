import os
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
client = MongoClient("mongodb+srv://irfandahusni:1234abcd@irfndcluster.dhjmc.mongodb.net/irfanDB?retryWrites=true&w=majority")
print("removing previous data ...")
client.irfanDB.irfanCollection.delete_many( { } )
try : 
    data = client.irfanDB.irfanCollection.find_one()
    if data == None:
        print("There is no data")
except :
    print("command error")
change_stream = client.irfanDB.irfanCollection.watch([{
    '$match': {
        'operationType': { '$in': ['insert'] }
    }
}])
print("start streaming ...")
i = 0
for change in change_stream:
    print("new data detected")
    i = i+1
    print("i value: ", i)
    print(dumps(change))
    print('') # for readability only
# cursor = client.irfanDB.irfanCollection.watch()
# document = next(cursor)