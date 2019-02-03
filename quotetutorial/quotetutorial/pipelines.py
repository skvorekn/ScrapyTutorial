# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# Scraped data -> item container -> pipeline -> SQL/Mongo database
# activate pipeline in settings.py

import sqlite3

class QuotetutorialPipeline(object):

    def __init__(self):
        # both functions are called automatically
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('myquotes.db')
        self.curr = self.conn.cursor()

    def create_table(self):

        self.curr.execute("""DROP TABLE IF EXISTS quotes_db""")
        self.curr.execute("""create table quotes_tb(
        title text,
        author text,
        tag text
        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipeline :" + item['title'][0])
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO quotes_tb VALUES (?,?,?)""",(
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()
        # don't need to close connect because many iterations
