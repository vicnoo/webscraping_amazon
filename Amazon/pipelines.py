# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymongo

# class AmazonPipeline(object):
#     def __init__(self):
#         self.conn = pymongo.MongoClient(
#             'localhost'
#             ,27017
#         )
#         db = self.conn['amazonTVs']
#         self.collection = db['tv_data']
#     def process_item(self, item, spider):
#         self.collection.insert(dict(item))
#         return item
#------------------------------using sqlite3 and mysql.connector to insert into mysql and sqlite3 to store in a db--------------------------
import sqlite3
import pymongo
import mysql.connector

class AmazonPipeline(object):

     def __init__(self):
         self.create_connection()
         self.create_table()


     def create_connection(self):
         #self.conn = sqlite3.connect("amazon_tvs.db")
         self.conn = mysql.connector.connect(
             host = 'localhost'
             ,user = 'vicnoo'
             ,passwd = 'Otieno@1125'
             ,database = 'amazon_tvs'
         )
         self.curr = self.conn.cursor()


     def create_table(self):
         self.curr.execute(""" DROP TABLE IF EXISTS tv_data """)

         self.curr.execute(""" CREATE TABLE tv_data(
              product_name text
              ,product_category text
             ,product_price text
              ,product_imagelink text
              ) """)

    
     def process_item(self, item, spider):
         self.store_db(item)
         #print("pipeline " + item['title'] [0])
         return item


     def store_db(self, item):
         self.curr.execute(""" INSERT INTO tv_data VALUES (%s,%s,%s)""",(      # in sqlite we use ? instead of %s
             item['product_name'] [0]
             ,item['product_category'] [0]
             ,item['product_price'] [0]
             ,item['product_imagelink'] [0]
         ))
        #  self.curr.execute(""" INSERT INTO tv_data VALUES (?,?,?)""",(      # in sqlite we use ? instead of %s
        #      item['product_name'] [0]
        #      ,item['product_category'] [0]
        #      ,item['product_price'] [0]
        #      ,item['product_imagelink'] [0]
        #  ))
         self.conn.commit()
