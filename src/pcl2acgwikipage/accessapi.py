from urllib import request,parse
import json
from http.client import HTTPResponse,HTTPException
import time

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
    query_data = {}
    off_set = 0
    max_offset = 0
    MaxRetry = 5
    # 提取搜索词
    for keyword in keywords:
        # 创建用于存储搜索结果的列表
        results = []
        while not max_offset - off_set == 0:             
            # 构建请求参数
            url_query["action"] = "query"
            url_query["list"] = "search"
            url_query["srlimit"] = 500
            url_query["srsearch"] = keyword
            url_query["sroffset"] = off_set

            # 构建请求数据
            request_data = request.Request(f"{baseurl}?{parse.urlencode(url_query)}")
            # 处理可能的错误码
            try:
                response:HTTPResponse = request.urlopen(request_data)
            except HTTPException as e:
                # 避免可能的 API 封禁导致任务超时
                if MaxRetry == 0:
                    break    
                else:
                    MaxRetry -= 1
                    #等待 5 分钟然后再试一次
                    time.sleep(5*60)
                    continue
                        
            
            encode_data = json.loads(response.read().decode("utf-8"))

            result = encode_data["query"]["search"]
            if result == "":
                off_set = max_offset
                continue
            else:
                max_offset = encode_data["query"]["searchinfo"]["totalhits"]
                if max_offset - off_set < 0:
                    off_set -= max_offset
                else:
                    off_set += 500
                results.append(result)
                # 等待一分钟然后继续
                time.sleep(60)

        # 每次搜索任务结束后等待十分钟，避免请求过快浪费 API 资源
        time.sleep(600)
        # 将搜索结果保存到字典内      
        query_data[keyword] = results
