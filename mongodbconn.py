#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[1]:


"""NoSQL Database is a non-relational Data Management System, that does not require a fixed schema.
It avoids joins, and is easy to scale. The major purpose of using a NoSQL database is for distributed 
data stores with humongous data storage needs. NoSQL is used for Big data and real-time web apps. For example,
companies like Twitter, Facebook and Google collect
terabytes of user data every single day."""

"""Mongodb:-
MongoDB is an open source NoSQL database management program. NoSQL is used as an alternative to traditional 
relational databases. NoSQL databases are quite useful for working with large sets of distributed data. 
MongoDB is a tool that can manage document-oriented information, store or retrieve information.
"""


# ANS2

# In[2]:


"""Schema-less Database: It is the great feature provided by the MongoDB. A Schema-less database means one collection can hold different types of documents in it. Or in other words, in the MongoDB database, a single collection can hold multiple documents and these documents may consist of the different numbers of fields, content, and size. It is not necessary that the one document is similar to another document like in the relational databases. Due to this cool feature, MongoDB provides great flexibility to databases.
Document Oriented: In MongoDB, all the data stored in the documents instead of tables like in RDBMS. In these documents, the data is stored in fields(key-value pair) instead of rows and columns which make the data much more flexible in comparison to RDBMS. And each document contains its unique object id.
Indexing: In MongoDB database, every field in the documents is indexed with primary and secondary indices this makes easier and takes less time to get or search data from the pool of the data. If the data is not indexed, then database search each document with the specified query which takes lots of time and not so efficient.
Scalability: MongoDB provides horizontal scalability with the help of sharding. Sharding means to distribute data on multiple servers, here a large amount of data is partitioned into data chunks using the shard key, and these data chunks are evenly distributed across shards that reside across many physical servers. It will also add new machines to a running database.
Replication: MongoDB provides high availability and redundancy with the help of replication, it creates multiple copies of the data and sends these copies to a different server so that if one server fails, then the data is retrieved from another server.
Aggregation: It allows to perform operations on the grouped data and get a single result or computed result. It is similar to the SQL GROUPBY clause. It provides three different aggregations i.e, aggregation pipeline, map-reduce function, and single-purpose aggregation methods
High Performance: The performance of MongoDB is very high and data persistence as compared to another database due to its features like scalability, indexing, replication, etc.
Advantages of MongoDB : 
 

It is a schema-less NoSQL database. You need not to design the schema of the database when you are working with MongoDB.
It does not support join operation.
It provides great flexibility to the fields in the documents.
It contains heterogeneous data.
It provides high performance, availability, scalability.
It supports Geospatial efficiently.
It is a document oriented database and the data is stored in BSON documents.
It also supports multiple document ACID transition(string from MongoDB 4.0).
It does not require any SQL injection.
It is easily integrated with Big Data Hadoop
Disadvantages of MongoDB : 
 

It uses high memory for data storage.
You are not allowed to store more than 16MB data in the documents.
The nesting of data in BSON is also limited you are not allowed to nest data more than 100 levels."""


# ANS3

# In[3]:


"""import pymongo
client = pymongo.MongoClient("mongodb+srv://pwskills:pwskills@cluster0.yrgsdmj.mongodb.net/?retryWrites=true&w=majority")
db = client.test

client = pymongo.MongoClient("mongodb+srv://pwskills:pwskills@cluster0.yrgsdmj.mongodb.net/?retryWrites=true&w=majority")


db = client['pwskills']
coll_create = db["my_record"]

"""


# ANS4

# In[4]:


"""client = pymongo.MongoClient("mongodb+srv://pwskills:pwskills@cluster0.yrgsdmj.mongodb.net/?retryWrites=true&w=majority")
db = client.test

client = pymongo.MongoClient("mongodb+srv://pwskills:pwskills@cluster0.yrgsdmj.mongodb.net/?retryWrites=true&w=majority")


db = client['pwskills']
coll_create = db["my_record"]


## inserting one record into the database:-

data = {"name" : "sudh",
        "class" : "data science masters ",
        "timing " : "flexi"
}

coll_create.insertOne(data)


##insertMany records into the datbase:-

 data3 = [
  { "name": "Amy", "address": "Apple st 652" },
  { "name": "Hannah", "address": "Mountain 21" },
  { "name": "Michael", "address": "Valley 345" },
  { "name": "Sandy", "address": "Ocean blvd 2" },
  { "name": "Betty", "address": "Green Grass 1" },
  { "name": "Richard", "address": "Sky st 331" },
  { "name": "Susan", "address": "One way 98" },
  { "name": "Vicky", "address": "Yellow Garden 2" },
  { "name": "Ben", "address": "Park Lane 38" },
  { "name": "William", "address": "Central st 954" },
  { "name": "Chuck", "address": "Main Road 989" },
  { "name": "Viola", "address": "Sideway 1633" }
]

coll_create.insertOne(data3)


## find():-

for i in coll_create.find():
    print(i)
    
    
##findOne:-

coll_create.find_one()


"""


# ANS5

# In[5]:


"""import pymongo
client = pymongo.MongoClient("mongodb+srv://pwskills:pwskills@cluster0.yrgsdmj.mongodb.net/?retryWrites=true&w=majority")
db = client.test

client = pymongo.MongoClient("mongodb+srv://pwskills:pwskills@cluster0.yrgsdmj.mongodb.net/?retryWrites=true&w=majority")


db = client['pwskills']

coll_create = db["my_record"]

data = {"name" : "sudh",
        "class" : "data science masters ",
        "timing " : "flexi"
}

coll_create.insert_one(data)

for i in coll_create.find():
    print(i)
"""


# ANS6

# In[6]:


"""The sort() method specifies the order in which the query returns the matching documents 
from the given collection. You must apply this method to the cursor before retrieving any documents
from the database. It takes a document as a parameter that contains a field: value pair that defines 
the sort order of the result set. The value is 1 or -1 specify an
ascending or descending sort respectively.


db.Collection_Name.sort({filed_name:1 or -1})
"""


# ANS7

# In[7]:


"""Delete_many()
Delete_many() is used when one needs to delete more than one document.
A query object containing which document to be deleted is created and is passed as the
first parameter to the delete_many().

collection.delete_many(filter, collation=None, hint=None, session=None)

Deletion Order
db.collection.deleteOne()
 deletes the first document that matches the filter. Use a field that is part of a unique index such as _id for precise deletions.


try {
   db.orders.deleteOne( { "_id" : ObjectId("563237a41a4d68582c2509da") } );
} catch (e) {
   print(e);
}

The drop() Method
MongoDB's db.collection.drop() is used to drop a collection from the database.

db.COLLECTION_NAME.drop()
"""


# In[ ]:




