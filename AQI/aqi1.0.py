"""
    AQI计算
    版本：v1.0
"""


def cal_linear(iaqi_low, iaqi_high, bp_low, bp_high, val):
    """
        范围缩放
    """
    iaqi = (iaqi_high - iaqi_low) * (val - bp_low) / (bp_high - bp_low) + iaqi_low
    return iaqi


def cal_pm_iaqi(pm_val):
    """
        计算pm2.5的IAQI
    """
    if 0 <= pm_val <= 35:
        iaqi = cal_linear(0, 50, 0, 35, pm_val)
    elif 35 < pm_val <= 75:
        iaqi = cal_linear(50, 100, 35, 75, pm_val)
    elif 75 < pm_val <= 115:
        iaqi = cal_linear(100, 150, 75, 115, pm_val)
    elif 115 < pm_val <= 150:
        iaqi = cal_linear(150, 200, 115, 150, pm_val)
    else:
        pass


def cal_co_iaqi(co_val):
    """
        计算CO的IAQI
    """
    if 0 <= co_val <= 2:
        iaqi = cal_linear(0, 50, 0, 2, co_val)
    elif 2 < co_val <= 2:
        iaqi = cal_linear(50, 100, 2, 4, co_val)
    elif 4 < co_val <= 14:
        iaqi = cal_linear(100, 150, 4, 14, co_val)
    elif 14 < co_val <= 24:
        iaqi = cal_linear(150, 200, 14, 24, co_val)
    else:
        pass


def cal_aqi(aqi_list):
    """
         AQI计算
    """
    pm_val = aqi_list[0]
    co_val = aqi_list[1]

    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaqi(co_val)

    aqi = pm_iaqi if pm_iaqi > co_iaqi else co_iaqi
    return aqi


def main():
    """
        主函数
    """
    print('请输入以下信息，用空格分隔')
    input_str = input('(1)pm2.5 (2)CO:')
    str_list = input_str.split(' ')
    pm_val = float(str_list[0])
    co_val = float(str_list[1])

    aqi_list = []
    aqi_list.append(pm_val)
    aqi_list.append(co_val)

    # 调用AQI计算函数
    aqi_val = cal_aqi(aqi_list)

    print('空气质量指数为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()
