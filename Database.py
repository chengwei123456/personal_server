import pymysql.cursors
from flask import jsonify
import json
import time

class SqlConnect:
    def __init__(self):
        # 打开数据库
        self.connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='624626',
            db='myarticles',
            charset='utf8'
        )
        # 获取游标
        self.cursor = self.connect.cursor()

    def insertData(self, title, contents, image, tags, read, message):
        """
        插入数据
        :return:
        """
        localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = "INSERT INTO blogs (title, `data`, contents, image, tags, `read`, message) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"
        data = (title, localtime, contents, image, tags, read, message)
        self.connect.ping(reconnect=True)
        self.cursor.execute(sql % data)
        self.connect.commit()
        print('成功插入')
    def Id_UpData(self,id,read):
        read = str(int(read) + 1)

        sql = "UPDATE blogs SET `read` = {} WHERE `id` = {}".format(read, str(id))
        self.connect.ping(reconnect=True)
        self.cursor.execute(sql)
        self.connect.commit()

    def search_id(self,ID):
        sql =  "select * from blogs where `id` = {}".format(ID)
        self.connect.ping(reconnect=True)
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        results = {}

        id = data[0]
        title = data[1]
        time = data[2]
        content = data[3]
        image = data[4]
        tag = data[5]
        read = data[6]
        message = data[7]

        results["id"] = id
        results["time"] = time
        results["title"] = title
        results["content"] = content
        results["image"] = image
        results["tag"] = tag
        results["read"] = read
        results["message"] = message
        return jsonify(results)
    def search(self,endId):
        """
        取出所有数据
        :return:
        """
        sql = "SELECT * from blogs ORDER BY `read` DESC limit 0, {}".format(endId)
        self.connect.ping(reconnect=True)
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        lists = []
        for data in datas:
            results = {}
            id = data[0]
            title = data[1]
            time = data[2]
            content = data[3]
            image = data[4]
            tag = data[5]
            read = data[6]
            message = data[7]

            results["id"] = id
            results["time"] = time
            results["title"] = title
            results["content"] = content
            results["image"] = image
            results["tag"] = tag
            results["read"] = read
            results["message"] = message
            lists.append(results)
        if len(lists) ==0:
            sql = "alter table blogs AUTO_INCREMENT=1"
            self.connect.ping(reconnect=True)
            self.cursor.execute(sql)
        return jsonify(lists)

    def dele_blog(self,id):
        sql = "DELETE FROM blogs WHERE `id`={}".format(id)
        self.connect.ping(reconnect=True)
        self.cursor.execute(sql)
        self.connect.commit()
        print("删除成功")
    def get_java_blogs(self, tag):
        sql = "select * from blogs where `tags`='{}'".format(tag)
        self.connect.ping(reconnect=True)
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        lists = []
        for data in datas:
            results = {}
            id = data[0]
            title = data[1]
            time = data[2]
            content = data[3]
            image = data[4]
            tag = data[5]
            read = data[6]
            message = data[7]

            results["id"] = id
            results["time"] = time
            results["title"] = title
            results["content"] = content
            results["image"] = image
            results["tag"] = tag
            results["read"] = read
            results["message"] = message
            lists.append(results)
        return jsonify(lists)
    # 获取各类博客的总数
    def get_blogs_count(self):
        sql = "select  tags,COUNT(*)  from blogs GROUP BY tags with rollup"
        self.connect.ping(reconnect=True)
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        result = {}
        for data in datas:
            result[data[0]] = data[1]
        return jsonify(result)
    # 按阅读量排序
    def readSort(self):
        sql = "SELECT * from blogs ORDER BY `read` DESC LIMIT 8"
        self.connect.ping(reconnect=True)
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        lists = []
        for data in datas:
            result = {}
            id = data[0]
            title = data[1]
            result['id'] = id
            result['title'] = title
            lists.append(result)
        return jsonify(lists)

if __name__ == '__main__':
    c = SqlConnect()
    c.search_id(48)
