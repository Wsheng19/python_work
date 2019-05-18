"""
    AQI计算
    版本：v6.0
"""
import requests
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
        获取城市的AQI
    """
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout=30)                 # timeout是等待连接时间
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', class_='span1')

    city_aqi = []
    for i in range(8):
        caption = div_list[i].find('div', class_='caption').text.strip()
        value = div_list[i].find('div', class_='value').text.strip()

        city_aqi.append((caption, value))
    return city_aqi


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市拼音：')
    city_aqi = get_city_aqi(city_pinyin)

    print(city_aqi)


if __name__ == '__main__':
    main()
