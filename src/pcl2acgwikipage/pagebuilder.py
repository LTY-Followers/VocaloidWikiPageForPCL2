import pathlib
from urllib import request,parse
from http.client import HTTPResponse

code = ""


http_ok = range(200,300)

headers = {
    "User-Agent":"PCL2VocaloidWikiPage/0.0.1(github.com/wuliaodexiaoluo/VocaloidWikiPageForPCL2) Author/wuliaodexiaoluo(wuliaodexiaoluo@outlook.com)",
    "Content-Type":"application/x-www-form-urlencoded",
    "Accept":"application/json"
}

baseurl = "https://zh.moegirl.org.cn/index.php"

url_query = {
    "action":"raw"
}

name = input()

url_query["title"] = name


def textblock():
    return f"<TextBlock />\n"
def Image(Source,HorizontalAlignment="center",Margin="0,0,0,6"):
    return f"<Image Margin={Margin} Source={Source} HorizontalAlignment={HorizontalAlignment} />\n"
def localImage(Source,FallbackSource="",HorizontalAlignment="center",Margin="0,0,0,6"):
    return f"<local:MyImage Margin={Margin} Source={Source} HorizontalAlignment={HorizontalAlignment} FallbackSource={FallbackSource} />\n"
def MyCard(title,Margin,CanSwap,IsSwaped):
    return f"<local:MyCard Title={title} Margin={Margin} CanSwap={str(CanSwap)} IsSwaped={str(IsSwaped)}>\n"