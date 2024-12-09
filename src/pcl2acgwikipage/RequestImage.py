from urllib import request,parse
from bs4 import BeautifulSoup
from PIL import Image

search_api = "https://search.bilibili.com/all"

url_query = {}

def ReadImage(bvid):
    url_query["keywords"] = bvid
def CoverImage(file_name):
    image.open()