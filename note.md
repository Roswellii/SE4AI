项目研究有一个超大规模的数据集

不想再用txt来存数据了

---

这是一点点大规模xml数据+python+mongoDB的笔记 --roswell 2022

---

[toc]

### mongoDB简介

1. 底层是c++
2. 支持的数据结构类似json
3. 查询语言强大，支持对数据建立索引
4. 是一种NoSQL 非关系型的数据存储    
5. 是一个文档型数据库。允许嵌套键值。
6. 术语上也与关系型数据库有区别：行= document， 列= field



### mongo.exe启动失败问题

参考 https://blog.csdn.net/chenjuqing168/article/details/86603030?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&utm_relevant_index=1



重新指定数据库路径：

"C:\Program Files\MongoDB\Server\4.2\bin\mongod.exe" --dbpath E:\MongoDB\Server\4.2\data

尚不理解问题的根源



### mongDB的常用操作

参考   https://www.cnblogs.com/aademeng/articles/9779271.html



### 用python操作MongDB的流程

#### 添加数据

1. 建立连接
2. 指定数据库
3. 指定集合（相当于关系型数据库的表）
4. 添加数据

#### 待续



### xml超大规模数据

python的xml.dom包要求先将xml读入内存再进行处理，显然几十G的数据是塞不下的。

应当使用xml.sax包，该包支持分步读取。

