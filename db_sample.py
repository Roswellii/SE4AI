# !/usr/bin/python3

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mongo_test']
mycol = mydb["students"]

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20190101',
    'name': 'amy',
    'age': 23,
    'gender': 'female'
}

# x = mycol.insert_one(student1)
# x = mycol.insert_one(student2)

result = mycol.find_one({'name': 'amy'})

print(result)
