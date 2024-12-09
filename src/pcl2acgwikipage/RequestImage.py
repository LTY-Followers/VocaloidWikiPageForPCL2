from urllib import request,parse
from bs4 import BeautifulSoup
from PIL import Image
from http.client import HTTPResponse
from http.client import HTTPException
import time

search_api = "https://search.bilibili.com/all"

url_query = {}

headers = {
    "User-Agent":"",
    "referer":"https://www.bilibili.com/",
    "Host":"search.bilibili.com"
}

MaxRetry = 5

async def ReadImage(bvid):
    url_query["keywords"] = bvid
    while not MaxRetry == 0:
        try:
            req = request.Request(url=f"{search_api}?{parse.urlencode(url_query)}",headers=headers)
            resp:HTTPResponse = request.urlopen(req)
        except HTTPException as e:
            time.sleep(5*60)
            continue
        resp_html = resp.read().decode("utf-8")
        soup = BeautifulSoup(resp_html,"html.parser")
        resolve = soup.find_all("img",loading="lazy")
        resolve.get("src")
def CoverImage(file_name):
    image.open()