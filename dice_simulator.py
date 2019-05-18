"""
    功能：模拟掷两个色子
          可视化掷两个色子的结果
          直方图可视化结果
"""
import random
import matplotlib.pyplot as plt
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def roll_dice():
    """
        模拟掷色子
    """
    return random.randint(1, 6)


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
    roll_list = []
    # roll2_list = []
    for i in range(try_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll_list.append(roll1 + roll2)
    #     roll1_list.append(roll1)
    #     roll2_list.append(roll2)
    #     roll_dict[roll1 + roll2] += 1
    # for i, result in roll_dict.items():
    #     print('点数{}的次数是：{}，其频率为{}'.format(i, result, result / try_times))
    # 数据可视化 alpha调节点的透明度  c改颜色  hist()
    # x = range(1, try_times + 1)
    # plt.scatter(x, roll1_list, c='red', alpha=0.5)
    # bins=是横坐标范围  edgecolor=是柱子中间的分解颜色 linewidth是分界线的宽度  normed=是计算频率
    plt.hist(roll_list, bins=range(2, 14), normed=1, edgecolor='black', linewidth=1)
    plt.title('色子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()
