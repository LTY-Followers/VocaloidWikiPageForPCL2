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

def reslove_page():
    req = request.Request(url=f"{baseurl}?{parse.urlencode(url_query)}",headers=headers)
    # 打开 Url
    resp:HTTPResponse = request.urlopen(req)
    # 检查状态码
    if resp.getcode() not in http_ok:
        raise RuntimeError(f"远程服务器返回错误:{resp.getcode()}")
    else:
        # 逐行读取内容
        lines = resp.readlines()
        line_num = 0
        line_num_dump = line_num
        for line in lines:
            line_num += 1
            #检查是否包含殿堂/传说/神话曲题头
            if "题头" in line.decode("utf-8"):
                code += '''
                <local:MyCard Title="Vocaloid Wiki For PCL" Margin="0,0,0,15" CanSwap="True" IsSwaped="False">\n
                    <StackPanel Margin="25,40,23,15">"   '''
                text = ""
                description_start = False
                # 循环读取每一段内容
                while "vocaloid_songbox" in content.lower():
                    # 计数器自增
                    line_num_dump += 1
                    content = resp.readline(line_num_dump).decode("utf-8")
                    if "{{cquote|<poem>" in content.lower():
                        # 移除 WikiText 代码
                        text += content.lower().replace("{{cquote|<poem>","").replace("\n","&#xA;").replace("　"," ") # 萌百的编辑者喜欢用全角空格，为了避免出 Bug 替换成半角的
                        description_start = True
                        continue
                    elif description_start and "</poem>}}" not in content.lower():
                        text += content.replace("\n","&#xA;")
                    else :
                        text += content.replace("\n","&#xA;").replace("</poem>}}","")
                if text == "":
                    # 没有内容
                    continue
                else:
                    code += '<TextBlock HorizontalAlignment="Center" Margin="0,0,0,0"\n   Foreground="{DynamicResource ColorBrush2}" FontSize="10"\n    Text="'+text+'" />'
                    # 重置计数器
                    play_num = 0
                    line_num_dump = line_num
                    software_name = ""
                    if "vocaloid" in line.decode("utf-8").lower():
                        software_name = "VOCALOID"
                    elif "ace" in line.decode("utf-8").lower():
                        software_name = "ACE"
                    if "殿堂" in line.decode("utf-8") and "|" not in line.decode("utf-8"):
                        level = " 殿堂"
                        play_num = "10"
                    elif "殿堂" in line.decode("utf-8") and "|" in line.decode("utf-8"):
                        play_num = line.decode("utf-8").replace()
                code += '<local:MyTextButton HorizontalAlignment="Center" Margin="0,15,0,0" FontSize="15" \
               Text="本曲在 bilibili 播放次数超过 '+play_num+' 万，获得 '+software_name+level+'曲称号" EventType="打开网页" EventData="https://zh.moegirl.org.cn/'+name+'" />'
            code += '<TextBlock HorizontalAlignment="Center" Margin="0,15,0,0" \
                \n  Foreground="{DynamicResource ColorBrush2}" FontSize="20" \n \
                Text="'+name+'" />'