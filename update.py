
import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['SOposts']
collection = mydb["post"]

results= collection.find(no_cursor_timeout = True)
i=0
for result in results:
    i+=1
    if("Tags" in result):
        tags = result["Tags"]
        if isinstance(tags,list):
            print("skip")
            continue
        else:
            print("*** updating at post " + str(i) + " ***")
            Id= result["Id"]
            tags = tags.replace("><", " ")
            tags = tags.replace("<", "")
            tags = tags.replace(">", "")
            tags_list = tags.split(" ")
            collection.update_one({"Id": Id}, {"$set": {"Tags": tags_list}})

print("done!")



