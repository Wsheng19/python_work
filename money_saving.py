"""
存钱
"""
import math
import datetime


def save_money_in_n_week(total_week, money_per_week, addition):
    money_list = []                                         # 记录每周存款数的列表
    save_money_list = []                                    # 记录n周存款金额
    for i in range(total_week):
        # 存钱
        money_list.append(money_per_week)
        total_saving = math.fsum(money_list)                # 存钱总数
        save_money_list.append(total_saving)
        # # 输出信息
        # print('第{}周，存入{}钱，共存入{}元'.format(i + 1, money_per_week, total_saving))
        # 更新信息
        money_per_week += addition
    return save_money_list


def main():
    """
    主函数 
    """
    money_per_week = float(input('请输入每周要存的钱：'))     # 每周要存的钱
    addition = float(input('请输入每周要多存的钱：'))           # 每周要多存的钱
    total_week = int(input('请输入总共的周数：'))         # 总共的周数
    # 调用函数
    total_saving_list = save_money_in_n_week(total_week, money_per_week, addition)
    # 输入日期
    date = input('请输入日期：（yyyy/mm/dd）')
    input_date = datetime.datetime.strptime(date, '%Y/%m/%d')
    week_num = input_date.isocalendar()[1]
    print('第{}周的存款金额为：{}元'.format(week_num, total_saving_list[week_num - 1]))


if __name__ == '__main__':
    main()
