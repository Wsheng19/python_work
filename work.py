import itchat
import time
import json
import requests
from bs4 import BeautifulSoup
from urllib import request, parse


def get_aqi(city_pinyin):
    """
        获取城市的AQI
    """
    url = 'http://pm25.in/' + city_pinyin
    try:
        r = requests.get(url, timeout=30)  # timeout是等待连接时间
        soup = BeautifulSoup(r.text, 'lxml')
        div_list = soup.find_all('div', class_='span1')

        city_aqi = []
        for i in range(8):
            caption = div_list[i].find('div', class_='caption').text.strip()
            value = div_list[i].find('div', class_='value').text.strip()

            city_aqi.append((caption, value))
        print(city_aqi)
        return city_aqi[0][1]
    except:
        return 'error'


def get_weather(city_pinyin):
    """
        获取城市的天气
    """
    url = 'https://www.tianqi.com/' + city_pinyin
    try:
        r = requests.get(url, timeout=60)  # timeout是等待连接时间
        soup = BeautifulSoup(r.text, 'lxml')
        weather = soup.find('dd', class_='weather').find('span').text.strip()
        print(weather)
        return weather
    except:
        return 'error'


def translate(content):
    """
        翻译
    """
    url = 'http://fanyi.youdao.com/translate'
    form_data = {}
    form_data['i'] = content
    form_data['doctype'] = 'json'

    data = parse.urlencode(form_data).encode('utf-8')  # 数据转换
    response = request.urlopen(url, data)  # 提交数据并解析
    html = response.read().decode('utf-8')  # 服务器返回结果读取
    # 可以看出html是一个json格式
    translate_results = json.loads(html)  # 以json格式载入
    translate_results = translate_results['translateResult'][0][0]['tgt']  # json格式调取
    return translate_results


@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:
        # 发送一条提示给文件助手
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')
        if msg['Text'][:2] == '天气':
            city_pinyin = msg['Text'][3:]
            aqi = get_aqi(city_pinyin)
            weather = get_weather(city_pinyin)
            return '该地区AQI为：{}，该地区天气情况为：{}'.format(aqi, weather)
        elif msg['Text'][:2] == '翻译':
            content = msg['Text'][3:]
            result = translate(content)
            return '翻译结果为：\n{}'.format(result)


if __name__ == '__main__':
    itchat.auto_login()

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()
