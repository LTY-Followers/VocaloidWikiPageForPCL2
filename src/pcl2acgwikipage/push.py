from requests import Session
from time import sleep

uri = "https://files.mirror.luolingxue.us.kg/api"
def UploadAPI(files:dict,session:Session):
    data = {
        "files":[]
    }

    for file,path in files.items():
        with open(path,"rb") as f:
            data["files"][file] = f 
        
    
    resp = session.post(url=uri+"/file/stream_upload",data=data)
    
    if resp.status_code == 202:
        resp_json = resp.json()
        task_id = resp_json["id"]
        while True:
            sleep(10)
            resp = session.get(url=uri+f"/file/stream_upload/status?pid={task_id}")
            
