"""
    功能：模拟掷两个色子
          可视化掷两个色子的结果
          直方图可视化结果
          科学计算
"""
import numpy as np
import matplotlib.pyplot as plt
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
    主函数
    """
    try_times = 10000
    # # 初始化列表
    # result_list = [0] * 11
    # roll_list = list(range(2, 13))
    # roll_dict = dict(zip(roll_list, result_list))
    # 记录色子的结果
    roll1_list = np.random.randint(1, 7, size=try_times)
    roll2_list = np.random.randint(1, 7, size=try_times)
    roll3_list = np.random.randint(1, 7, size=try_times)
    roll_list = roll1_list + roll2_list + roll3_list

    hist, bins = np.histogram(roll_list, bins=range(3, 20))
    print(hist)
    print(bins)
    # roll2_list = []
    #     roll1_list.append(roll1)
    #     roll2_list.append(roll2)
    #     roll_dict[roll1 + roll2] += 1
    # for i, result in roll_dict.items():
    #     print('点数{}的次数是：{}，其频率为{}'.format(i, result, result / try_times))

    # 数据可视化 alpha调节点的透明度  c改颜色  hist()
    # x = range(1, try_times + 1)
    # plt.scatter(x, roll1_list, c='red', alpha=0.5)
    # bins=是横坐标范围  edgecolor=是柱子中间的分解颜色 linewidth是分界线的宽度  normed=是计算频率 rwidth=是间隙

    # 设置X轴坐标显示
    tick_lable = ['3点', '4点', '5点', '6点', '7点', '8点', '9点', '10点', '11点', '12点', '13点', '14点',
                  '15点', '16点', '17点', '18点']
    tick_pos = np.arange(3.5, 19.5)
    plt.xticks(tick_pos, tick_lable)

    plt.hist(roll_list, bins=range(3, 20), normed=1, edgecolor='black', linewidth=1, rwidth=0.8)
    plt.title('色子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()
