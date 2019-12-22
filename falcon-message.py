# -*- coding: utf-8 -*-
from flask import Flask ,request
import requests
import json
import urllib.parse
import re
import logging

app = Flask(__name__)
logging.basicConfig(filename="./dingtalk.log",format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
open = open("seting.json",encoding='utf-8')
seting = json.load(open)

line_url = "https://api.line.me/v2/bot/message/push"

@app.route('/api/line',methods=['POST','GET'])
def falcon_message():
    falcon_messages = request.get_data()
    falcon_messages.decode(encoding='gbk')
    res = urllib.parse.unquote(str(falcon_messages))

    error_status = res.split("'")[1].split("[")[2].split("]")[0]   #异常状态
    server_name = res.split("'")[1].split("[")[3].split("]")[0]  #主机名称
    error_chinese = res.split("'")[1].split("[")[5].split('+all')[0].replace('+',' ')   #报警中文内容 此为templates里设置的note部分
    error_value = res.split("'")[1].split("[")[5].split(')+')[1].replace('+',' ').split(']')[0] #报警数值
    time = res.split("'")[1].split("[")[6].split("]")[0].split("+")[1] + " " + \
           res.split("'")[1].split("[")[6].split("]")[0].split("+")[2]

    if error_status == "PROBLEM":
        error_status = "状态异常"
    elif error_status == "OK":
        error_status = "状态恢复"

    aa = res.split("'")[1].split('&')
    for item in aa:
        if re.match(r'^tos=', item):
            api_key = item.split("=")[1].split((','))
            for i in range(len(api_key)):
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + '{' + api_key[i] + '}'
                }
                message = {
                    "to":seting["master_userID"],
                    "messages":[{
                    "type": "text",
                    "text": error_status + "\n" +
                            "报警主机： " + server_name + "\n" +
                            "错误信息 :" + error_chinese + "\n" +
                            "报警数值: " + error_value + "\n" +
                            "报警时间: " + time
                }]
                }
                requests.post(url=line_url,headers=headers,data=json.dumps(message))

    return falcon_messages

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)