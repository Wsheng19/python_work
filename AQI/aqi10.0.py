"""
    AQI计算
    版本：v7.0
"""
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


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

    # top50 kind为图的类型(line是折线图),(bar是柱状图)
    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='line', x='City', y='AQI', title='空气质量最好的50个城市', figsize=(20, 10))
    plt.savefig('top50_aqi_line.png')
    plt.show()


if __name__ == '__main__':
    main()
