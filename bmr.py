"""
    BMR计算器
"""


def bmr_calculator(g, w, h, a):
    if g == '男':
        bmr = (13.7 * w) + (5.0 * h) - (6.8 * a) + 66
        print('您的基础代谢率为：{}大卡'.format(bmr))
    elif g == '女':
        bmr = (9.6 * w) + (1.8 * h) - (4.7 * a) + 655
        print('您的基础代谢率为：{}大卡'.format(bmr))
    else:
        print('输入性别有误')


def main():
    """
    主函数
    """
    # 性别
    gender = input('请输入性别(退出请输入Q)： ')
    while gender != 'Q':
        try:
            # 体重
            weight = float(input('请输入体重（kg）： '))
            # 身高
            height = float(input('请输入身高（cm）： '))
            # 年龄
            age = int(input('请输入年龄： '))
            bmr_calculator(gender, weight, height, age)
            # 性别
            gender = input('请输入性别(退出请输入Q)： ')
        except ValueError:
            print('请输入信息的正确形式！')
        except:
            print('程序异常!')
    print('程序已退出')


if __name__ == '__main__':
    main()
