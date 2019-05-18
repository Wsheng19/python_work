"""
    AQI计算
    版本：v7.0
"""
import pandas as pd


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('all_city_aqi.csv')
    # print(aqi_data.head(5))
    # print(aqi_data[['City', 'AQI']].head(5))
    print('基本信息：')
    print(aqi_data.info())
    print('数据预览：\n{}'.format(aqi_data.head()))

    # 数据清洗 只保留AQI>0的数据
    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    # 基本统计
    print('AQI的最大值是：{}'.format(clean_aqi_data['AQI'].max()))
    print('AQI的最小值是：{}'.format(clean_aqi_data['AQI'].min()))
    print('AQI的均值是：{}'.format(clean_aqi_data['AQI'].mean()))

    # top10
    top10_cities = clean_aqi_data.sort_values(by=['AQI']).head(10)
    print('空气质量最好的10个城市：\n{}'.format(top10_cities))

    # bottom10
    # bottom10_cities = clean_aqi_data.sort_values(by=['AQI']).tail(10)
    bottom10_cities = clean_aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print('空气质量最差的10个城市：\n{}'.format(bottom10_cities))

    # 保存csv文件
    top10_cities.to_csv('top10_cities.csv', index=False)
    bottom10_cities.to_csv('bottom10_cities.csv', index=False)


if __name__ == '__main__':
    main()
