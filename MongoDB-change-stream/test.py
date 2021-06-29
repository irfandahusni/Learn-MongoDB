import pymongo
from pymongo import MongoClient 
import datetime
import os

client = MongoClient("mongodb+srv://irfandahusni:1234abcd@irfndcluster.dhjmc.mongodb.net/irfanDB?retryWrites=true&w=majority")

dbCol = client.irfanDB.irfanCollection

print("testpy : Inserting Data ...")

dbCol.insert_one({"_id": 1, "hello": "world"})
# dbCol.update_one({"_id": 1}, {"$set": {"hello": "mars"}})
# dbCol.replace_one({"_id": 1} , {"bye": "world"})
# dbCol.delete_one({"_id": 1})
# dbCol.drop()