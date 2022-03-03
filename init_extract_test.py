
import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mongo_test']
collection = mydb["students"]

myquery = {'gender': 'male'}
newvalue= { "$set": { "gender": 12345 } }

status = collection.update_one(myquery, newvalue)
print(status)

for i in collection.find():
    print(i)




