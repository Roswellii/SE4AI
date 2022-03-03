
import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['SOposts']
collection = mydb["post"]

rows = collection.find().sort('_id', -1).limit(1)  # 倒序以后，只返回1条数据

for row in rows:  # 这个循环只会执行1次
    print(row)
