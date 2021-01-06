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
        print("更新成功")

    def search(self):
        """
        取出所有数据
        :return:
        """
        sql = "select * from blogs"
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

    def dele_blog(self,id):
        sql = "DELETE FROM blogs WHERE `id`={}".format(id)
        self.connect.ping(reconnect=True)
        self.cursor.execute(sql)
        self.connect.commit()
        print("删除成功")
if __name__ == '__main__':
    c = SqlConnect()
    c.Id_InsertData(5,100)
