"""
    AQI计算
    版本：v7.0
"""
import csv
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
        # caption = div_list[i].find('div', class_='caption').text.strip()
        value = div_list[i].find('div', class_='value').text.strip()

        # city_aqi.append((caption, value))
        city_aqi.append(value)
    return city_aqi


def get_all_cities():
    """
        获取所有城市
    """
    url = 'http://pm25.in/'
    city_list = []
    r = requests.get(url, timeout=30)                 # timeout是等待连接时间
    soup = BeautifulSoup(r.text, 'lxml')

    city_div = soup.find_all('div', class_='bottom')[1]
    city_link_list = city_div.find_all('a')
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href'][1:]
        city_list.append((city_name, city_pinyin))
    return city_list


def main():
    """
        主函数
    """
    city_list = get_all_cities()
    # for city in city_list:
    #     city_name = city[0]
    #     city_pinyin = city[1]
    #     city_aqi = get_city_aqi(city_pinyin)
    #     print(city_name, city_aqi)
    header = ['City', 'AQI', 'PM2.5/1h', 'PM10/1h', 'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h']
    with open('all_city_aqi.csv', 'w', encoding='utf-8', newline='') as f:
        csv.writer(f).writerow(header)
        for i, city in enumerate(city_list):
            city_name = city[0]
            city_pinyin = city[1]
            city_aqi = get_city_aqi(city_pinyin)
            row = [city_name] + city_aqi
            csv.writer(f).writerow(row)

            if (i + 1) % 10 == 0:
                print('\r共收集了{}条消息'.format(i + 1), end='')


if __name__ == '__main__':
    main()
