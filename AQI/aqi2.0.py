"""
    AQI计算
    版本：v2.0
"""
import json


def process_jsonfile(filepath):
    """
        解码json文件
    """
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    f.close()
    return city_list


def main():
    """
        主函数
    """
    filepath = input('请输入json文件名称：')
    city_list = process_jsonfile(filepath)
    city_list.sort(key=lambda city: city['aqi'])
    top2_list = city_list[:2]

    f = open('top5_aqi.json', mode='w', encoding='utf-8')
    json.dump(top2_list, f, ensure_ascii=False)
    f.close()
    print(city_list)


if __name__ == '__main__':
    main()
