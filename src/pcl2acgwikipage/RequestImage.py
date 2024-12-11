# 一堆库
from urllib import request,parse
from bs4 import BeautifulSoup
from PIL import Image
from http.client import HTTPResponse,HTTPException
import time
import pathlib
import json

# bilibili Web 页面搜索接口
bili_search_html_api = "https://search.bilibili.com/all"
# bilibili API
bili_search_json_api = "https://api.bilibili.com/x/web-interface/search/type?"
# SMMS API
smmsapi="https://smms.app/api/v2"
# Url 查询参数
url_query = {}
# WebP 转码选项

options = {
    "quality": 85,  
    "lossless": True,  # 显然图片质量必须足够高
    "transparency": True, 
}
# 适用于 bilibili 的请求头
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "referer":"https://www.bilibili.com/",
    "Host":"search.bilibili.com"
}
# 从 HTML 页面获取图片地址
def ReadImageUriFromHTML(bvid):
    # 使用 bvid 搜索防止一些二创版本的图片被爬进数据库里，反正使用 bvid 搜索结果永远只有一个
    # 避免死锁
    MaxRetry = 5
    url_query["keyword"] = bvid
    #避免 API 封禁或请求格式错误导致任务死锁，如果真让一个任务连续运行了 6h+ 后面就没时间提交了
    while not MaxRetry == 0:
        try:
            req = request.Request(url=f"{bili_search_html_api}?{parse.urlencode(url_query)}",headers=headers)
            resp:HTTPResponse = request.urlopen(req)
        except HTTPException as e:
            MaxRetry -= 1
            # 可能被 API 封禁
            time.sleep(1*60)
            continue
        resp_html = resp.read().decode("utf-8")
        # 解析页面
        soup = BeautifulSoup(resp_html,"html.parser")
        resolve = soup.find_all("img",loading="lazy")
        for source in resolve:
            # 通常 web-search-common-cover 才是视频封面
            if "web-search-common-cover" in source["src"]:
                img_direct_url = source["src"]
                return "https:" + img_direct_url.split("@")[0]
    return ""
# 图片转 WebP 节约流量
def CoverImage(file_name,new_file_name):
    path = pathlib.Path().cwd().joinpath("database",file_name)
    image_handle = Image.open(path)
    image_handle.save(path.replace(file_name,new_file_name),format="webp",options=options)

# 上传到 SMMS
def UploadImage(filename,auth_key):
    path = pathlib.Path().cwd().joinpath("database",filename)
    headers = {
        "Authorization":auth_key,
        "Content-Type":"multipart/form-data",
        "User-Agent":"PCL2VocaloidWikiPage/0.0.1(github.com/wuliaodexiaoluo/VocaloidWikiPageForPCL2) Author/wuliaodexiaoluo(wuliaodexiaoluo@outlook.com)"
    }
    data = {
        "smfile":open(path,"rb"),
        "format":"json"
    }
    req = request.Request(url=smmsapi+"/upload",headers=headers,data=data)
    try:
        resp:HTTPResponse = request.urlopen(req)
    except HTTPException as e:
        return False,resp
    resp_json = json.loads(resp.read().decode("utf-8"))
    if resp_json["success"]:
        img_direct_url = resp_json["data"]["url"]
        img_delete_api = resp_json["data"]["delete"]
        img_hash = resp_json["data"]["hash"]
        return True,""
    else:
        return False,resp

# 删除图片
def delete_img(img_delete_api,auth_key):
    headers = {
        "Authorization":auth_key,
        "Content-Type":"multipart/form-data",
        "User-Agent":"PCL2VocaloidWikiPage/0.0.1(github.com/wuliaodexiaoluo/VocaloidWikiPageForPCL2) Author/wuliaodexiaoluo(wuliaodexiaoluo@outlook.com)"
    }
    req = request.Request(url=img_delete_api,headers=headers)
    try:
        resp:HTTPResponse = request.urlopen(req)
    except HTTPException as e:
        return False,resp
    
    resp_json = resp.read().decode("utf-8")
    if resp_json["success"]:
        return True,""
    else:
        return False,resp