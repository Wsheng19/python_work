"""
    AQI计算
    版本：v5.0
"""
import requests


def get_html_text(url):
    """
        返回url的文本
    """
    r = requests.get(url, timeout=30)            # timeout是等待连接时间
    # print(r.status_code)
    return r.text


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市拼音：')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)
    url_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    begin_index = url_text.find(url_div) + len(url_div)
    end_index = begin_index + 2
    aqi_value = url_text[begin_index: end_index]
    print('空气质量为：{}'.format(aqi_value))


if __name__ == '__main__':
    main()
