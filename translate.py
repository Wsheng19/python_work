"""
    功能：对微信好友的消息进行翻译
"""
import json
import itchat
import re
from itchat.content import *
 
from urllib import request, parse


def translate(userName, content):
    req_url = 'http://fanyi.youdao.com/translate'  # 创建连接接口
    # 创建要提交的数据
    Form_Date = {}
    Form_Date['i'] = content  # 输入要翻译的内容
    Form_Date['doctype'] = 'json'
 
    data = parse.urlencode(Form_Date).encode('utf-8')  # 数据转换
    response = request.urlopen(req_url, data)  # 提交数据并解析
    html = response.read().decode('utf-8')  # 服务器返回结果读取
    # 可以看出html是一个json格式
    translate_results = json.loads(html)  # 以json格式载入
    translate_results = translate_results['translateResult'][0][0]['tgt']  # json格式调取
    print(translate_results)  # 输出结果
 
    itchat.send(translate_results, toUserName=userName)              # 发送翻译结果
 
 
# 如果对方发的是文字，则我们给对方回复以下的东西
@itchat.msg_register([TEXT])
def text_reply(msg):
    match = msg['Text']
    if match:
        content = msg['Text'][msg['Text'].find("+")+1:]
        translate(msg['FromUserName'], content)
       

itchat.auto_login()
itchat.run()
