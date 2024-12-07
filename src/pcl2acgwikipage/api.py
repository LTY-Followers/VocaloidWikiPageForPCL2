import sys
import pathlib
from urllib import request,parse
import logging

sys.path.append(pathlib.Path.cwd())

from loginapi import login

"""
try:
    baseurl = "https://zh.moegirl.org.cn/api.php"
    response = request.Request(url=baseurl+"?action=query&meta=token")
    data = {
        "lgname":"LuoYofu@wuliaodexiaoluo",
        "lgpassword":"q46gfidckt674atpmis3h0t9oc160v1b"
    }
    
    request.Request()
except Exception as e:
    
    exit(e)
"""

login(usrname="LuoYofu@wuliaodexiaoluo",password="q46gfidckt674atpmis3h0t9oc160v1b")