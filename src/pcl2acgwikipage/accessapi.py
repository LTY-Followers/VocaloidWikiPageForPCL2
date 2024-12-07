from urllib import request,parse
import json
from http.client import HTTPResponse,HTTPException

baseurl = "https://zh.moegirl.org.cn/api.php"

post_headers = {
    "User-Agent":"PCL2VocaloidWikiPage/0.0.1(github.com/wuliaodexiaoluo/VocaloidWikiPageForPCL2) Author/wuliaodexiaoluo(wuliaodexiaoluo@outlook.com)",
    "Content-Type":"application/x-www-form-urlencoded",
    "Accept":"application/json"
}

url_query={
    "format":"json"
}

http_ok = range(200,300)

async def search(keywords:list=["洛天依","乐正绫","言和","初音未来"]):
    # 构建请求参数
    off_set = 0
    for keyword in keywords:
        url_query["action"] = "query"
        url_query["list"] = "search"
        url_query["srlimit"] = 500
        url_query["srsearch"] = keyword
        url_query["sroffset"] = off_set

        request_data = request.Request(baseurl+parse.urlencode(url_query))

        response:HTTPResponse = request.urlopen(request_data)
        if response.getcode() not in http_ok:
            raise HTTPException("远程服务器")
        else:
            encode_data = json.loads(response.read().decode("utf-8"))




        # 提交 Query 搜索请求


        # 处理搜索结果

        # 写入索引文件

        # 回调