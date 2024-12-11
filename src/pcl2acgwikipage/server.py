from flask import Flask,make_response,abort,request
import pathlib
import json
import random


PCLPagePath = ["database","PCL2","Page"]

database = pathlib.Path().cwd().parent.joinpath("databse","index.json")


with open(database,"r") as f:
    data = json.loads(f.read())

app = Flask.name(__name__)

bind_url = ["https://pclhomeplazaoss.lingyunawa.top:20639","https://vocaloidwikipage.mirror.luolingxue.us.kg","https://cloudflaretunnel.luolingxue.us.kg"]

@app.route("/api/<path>")
def resolve_request(path):
    match path:
        case "acgwiki":
            pagelist:list = data["acgwiki"]["formats"]["pcl2page"]
            with open(random.choice(pagelist),"r") as f:
                if "Mozilla" in request.user_agent:
                    response = make_response()
                    response.status = 301
                    response.headers["location"] = "https://github.com/LTY-Followers/VocaloidWikiPageForPCL2/"
                    response.content_type = "text/html"
                    response.headers["server"] = "VocaloidWikiPageHTTPServer/0.1.0(Based on Python Flask)"
                if not request.url_root in bind_url:
                    with open("./html/403.html") as hf:
                        response = make_response(hf.read().replace("${reason}","使用的 Url 不在请求白名单中").replace("${solve}","请前往<a href='https://github.com/LTY-Followers/VocaloidWikiPageForPCL2'>项目地址</a>获取正确的地址").encode("utf-8"))
                        response.status = 403
                if request.user_agent:
                    response = ""
                response = make_response(f.read().encode("utf-8"))
                response.status = 200
                return response
                