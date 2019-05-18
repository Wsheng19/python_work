def converter_currency(im, er):
    out = im * er
    return out


def main():
    # 货币比例
    vs = 6.77
    # 输入带单位的货币金额
    currency = input("请输入带单位的货币金额(退出请输入Q)：")

    while currency != 'Q':
        # 获取货币单位及数值
        unit = currency[-3:]
        # 进行判断
        if unit in ['CNY', 'cny']:
            exchange_rate = 1 / vs
        elif unit in ['USD', 'usd']:
            exchange_rate = vs
        else:
            exchange_rate = -1
        if exchange_rate != -1:
            in_money = eval(currency[:-3])
            out_money = converter_currency(in_money, exchange_rate)
            print('转换后的金额：', out_money)
        else:
            print('暂时不支持该种货币转换！')
        # 输入带单位的货币金额
        currency = input("请输入带单位的货币金额(退出请输入Q)：")
    print('已退出！')


if __name__ == '__main__':
    main()
