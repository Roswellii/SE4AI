import xml.sax
import pymongo


k= 1
class MyHandler(xml.sax.ContentHandler):
    #初始化
    def __init__(self):
        print('init')
        #文件开始读
    def startElement(self,name,attrs):
        global k
        k+=1
        if(k<45806997): # 22.2.25 数据库崩溃 从崩溃点恢复写入
            return

        if attrs.__len__() > 0:
            try:
                doc= {} # mongoDB要求以字典的形式插入一行数据
                names= attrs.getNames() # 获取xml文档中一行数据的属性名, 保存在list里
                for name in names:
                    value= attrs.getValue(name) # 用属性名索引数据
                    doc[name]= value
                mycol.insert_one(doc)
                print("post "+ k +"inserted")
            except BaseException:
                return

        else:
            print(name, "节点不包含属性")


myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['SOposts']
mycol = mydb["post"]

parse=xml.sax.make_parser()
parse.setContentHandler(MyHandler())
parse.parse("E:\stackoverflow.com-Posts\Posts.xml")
print("done!")

