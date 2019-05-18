"""
判断某一天是这一年的第几天
"""
from datetime import datetime


def main():
    """
    主函数
    """
    date_str = input('请输入日期（yyyy/mm/dd）：')
    date = datetime.strptime(date_str, '%Y/%m/%d')
    year = date.year
    month = date.month
    day = date.day
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        days_in_month_list[1] += 1
    days = sum(days_in_month_list[:month - 1]) + day

    print('这是{}年的第{}天'.format(year, days))


if __name__ == '__main__':
    main()
