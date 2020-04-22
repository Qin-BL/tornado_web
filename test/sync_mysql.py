# -*- coding: utf-8 -*-
import codecs
import json
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors


class MysqlTwistedPipeline(object):
    """docstring for MysqlTwistedPipeline"""

    # 采用异步的机制写入mysql
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)  # 处理异常
        return item

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        # insert_sql, params = item.get_insert_sql()
        # print (insert_sql, params)
        # cursor.execute(insert_sql, params)
        insert_sql = """
            		insert into jobbole_article(title, url, create_date, fav_nums, url_object_id)
            		VALUES (%s, %s, %s, %s, %s)
        	"""
        # 可以只使用execute，而不需要再使用commit函数
        cursor.execute(insert_sql,
                       (item["title"], item["url"], item["create_date"], item["fav_nums"], item["url_object_id"]))

