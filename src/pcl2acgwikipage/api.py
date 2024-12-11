import importlib
import sys
from requests import get,head,post



check = False

for argument in sys.argv:
    if argument == "checkstroage":
        check=True
    elif "server" in argument:
        server_list = argument.replace("--server=","").split(";")
    elif "login" in argument:
        api_token = argument.replace("--login=","")
    else:
        continue
        
def checkstroage():
    headers = {
        "Authorization":api_token
    }
    for server in server_list:
        resp = get(f"https://{server}/api/profile/stroage",headers=headers)
        meta_info = resp.json()
        meta_info["space"]

if check: checkstroage()

async def start():
    accessapi = importlib.import_module(".accessapi")
    pagebuilder =importlib.import_module(".pagebuilder")
    RequestImage = importlib.import_module(".RequestImage")