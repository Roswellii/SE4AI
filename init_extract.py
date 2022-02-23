
#导入sax模块
import xml.sax
import os

titleFile= open('E:\output\init_extract.txt', 'a')

class MyHandler(xml.sax.ContentHandler):
    #初始化
    def __init__(self):
        print('init')
        #文件开始读
    def startElement(self,name,attrs):
        if attrs.__len__() > 0:
            try:
                posttype = attrs.getValue('PostTypeId')
                if(posttype=='2'):
                    return  # skip answers

                tags = attrs.getValue('Tags')
                body= attrs.getValue('Body')
                # if ("tensorflow" not in tags and "Tensorflow" not in tags and "Tensorflow" not in body and "Tensorflow" not in body):
                if ("tensorflow" not in tags and "Tensorflow" not in tags ):
                    return  # skip posts that does not contain Tensorflow in tags

                id= attrs.getValue('Id')
                title= attrs.getValue('Title')
                if ('How' in title or 'how' in title):
                        titleFile.write(id + " " + title + '\n')
            except BaseException:
                return

        else:
            print(name, "节点不包含属性")


parse=xml.sax.make_parser()
parse.setContentHandler(MyHandler())
parse.parse("Posts.xml")

