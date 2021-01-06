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
        image = 'http://www.lzqcode.com/images/java.jpg'
        database.insertData(title, content, image, tag, 0, 0)
        return "Success"
    else:
        return "Failure"


@app.route("/search",methods=['post'])
@cross_origin()
def Search_Blog():
    print("--------------------------------------------------")
    blogs = database.search()
    return blogs

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


if __name__ == '__main__':
    database = SqlConnect()

    app.run(host='0.0.0.0',port=80,debug=True)
    CORS(app, supports_credentials=True)