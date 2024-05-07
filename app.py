from flask import Flask, redirect
from Appconfig.Log import Log
from Appconfig.get_mysql_data import GetData
from flask import render_template
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')


@app.before_request
def before_request():
    ip = request.remote_addr
    with open("./logs/ip.txt", "a", encoding="utf-8") as f:
        f.write(ip + "\n")
    if ip == '14.106.53.152':
        redirect("/index")
    if int(ip.split(".")[1]) > 100:
        redirect("/index")
    else:
        return None


@app.route('/index/')
def index():
    return render_template("index.html")


@app.route("/object")
def object_name():
    # get_obj = request.args.get("object")
    get_obj = request.args.get("object")
    data = GetData()
    name = data.get_names(get_obj)
    # data.close()
    return render_template("mvindex.html", name=name, obj=get_obj, data=None)


@app.route("/detail")
def detail():
    id = request.args.get("id")
    obj = request.args.get("obj")
    table = GetData()

    math_data = table.get_names("math")
    math_json = {"name": "数学", "data": math_data}

    english_data = table.get_names("english")
    english_json = {"name": "英语", "data": english_data}

    computer_data = table.get_names("computer")
    computer_json = {"name": "计算机", "data": computer_data}

    object_data = [math_json, english_json, computer_json]

    url = table.get_url(int(id), obj)

    return render_template("detail.html", videoId=id, obj=obj, url=url, object_data=object_data)


@app.route("/Other")
def other():
    return render_template("other.html")


@app.route("/system-configurations-my", methods=['POST'])
def system():
    datas = request.get_json()
    data = datas
    # with open("./logs/data.txt", "a", encoding="utf-8") as f:
    #     f.write(datas["data"])
    return {
        "status": 200
    }


if __name__ == '__main__':
    log = Log()
    app.run(debug=True)
