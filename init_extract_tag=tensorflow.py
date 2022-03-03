
import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['SOposts']
collection = mydb["post"]

result= collection.find_one()
tags= result["Tags"]
print(type(tags))
print(tags)
tags= tags.replace("><", " ")
tags= tags.replace("<", "")
tags= tags.replace(">", "")
tags_list= tags.split(" ")
print(tags_list)



