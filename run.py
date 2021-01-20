from flask import Flask, request
from flask_cors import cross_origin
from flask_cors import CORS

from Database import SqlConnect
app = Flask(__name__)

@app.route("/insert", methods=["post"])
@cross_origin()
def Insert_Blog():
    data = request.get_json(silent=True)
    if data:
        title = data['title']
        content = data['content']
        tag = data['tag']
        print(tag)
        if tag == "java":
            image = 'http://www.lzqcode.com/images/java.jpg'
        elif tag =="前端":
            image = "http://www.lzqcode.com/images/web.jpg"
        elif tag =="Python":
            image = "https://bkimg.cdn.bcebos.com/pic/42166d224f4a20a44623921916188f22720e0df37a90?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2UxNTA=,g_7,xp_5,yp_5"
        elif tag =="PHP":
            image = "https://bkimg.cdn.bcebos.com/pic/8d5494eef01f3a292df50d57096fab315c6034a8d65d?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2U4MA==,g_7,xp_5,yp_5"
        else:
            image = "https://bkimg.cdn.bcebos.com/pic/8d5494eef01f3a29a0951bc49725bc315c607c5f?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2U4MA==,g_7,xp_5,yp_5"
        database.insertData(title, content, image, tag, 0, 0)
        return "Success"
    else:
        return "Failure"


@app.route("/search",methods=['post'])
@cross_origin()
def Search_Blog():
    data = request.get_json(silent=True)
    endId = data['endID']

    blogs = database.search(endId)
    return blogs

@app.route("/search_id",methods=['post'])
@cross_origin()
def search_id():
    data = request.get_json(silent=True)
    print(data)
    id = data['id']
    result = database.search_id(id)
    return result

@app.route("/get_java_blogs", methods=['post'])
@cross_origin()
def get_java_blogs():
    data = request.get_json(silent=True)
    tag = data["tag"]
    java_blogs = database.get_java_blogs(tag)
    return java_blogs

@app.route("/get_web_blogs",methods=['post'])
@cross_origin()
def get_web_blogs():
    data = request.get_json(silent=True)
    tag = data['tag']
    web_blogs = database.get_java_blogs(tag)
    return web_blogs
@app.route("/get_python_blogs",methods=['post'])
@cross_origin()
def get_python_blogs():
    data = request.get_json(silent=True)
    tag = data['tag']
    python_blogs = database.get_java_blogs(tag)
    return python_blogs

@app.route("/get_php_blogs",methods=['post'])
@cross_origin()
def get_php_blogs():
    data = request.get_json(silent=True)
    tag = data['tag']
    php_blogs = database.get_java_blogs(tag)
    return php_blogs

@app.route("/get_other_blogs",methods=['post'])
@cross_origin()
def get_other_blogs():
    data = request.get_json(silent=True)
    tag = data['tag']
    other_blogs = database.get_java_blogs(tag)
    return other_blogs

@app.route("/id_UpData",methods=["post"])
@cross_origin()
def Id_UpData():
    data = request.get_json(silent=True)
    if data:
        id = data["id"]
        read = data["read"]
        database.Id_UpData(id,read)
        return "success"
    else:
        return 'Failure'

@app.route("/dele_Data", methods=["post"])
@cross_origin()
def Dele_Data():
    data = request.get_json(silent=True)
    id = data["id"]
    database.dele_blog(id)
    return "success"

@app.route("/get_blogs_count",methods=["post"])
@cross_origin()
def get_blogs_count():
    result = database.get_blogs_count()
    return result

@app.route("/read_sort",methods=["post"])
@cross_origin()
def read_sort():
    result = database.readSort()
    return result

if __name__ == '__main__':
    database = SqlConnect()

    app.run(host='0.0.0.0',port=80,debug=True)
    CORS(app, supports_credentials=True)