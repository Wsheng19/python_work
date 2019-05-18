from numpy import *


def matrix_input():
    try:
        err = 0
        matrix = []
        row, column = eval(input('请依次输入矩阵的行和列(中间用英文逗号隔开)'))
        print('请逐行输入矩阵的数据（元素之间用逗号隔开，输完一行元素按一下回车）')
        for i in range(row):
            tup = eval(input())
            list_1 = list(tup)
            if len(list_1) == column:
                matrix.append(list_1)
            elif len(list_1) != 0:
                print('输入错误,请重新输入')
                err = 1
                break
        if err:
            return mat(matrix_input())
        else:
            return mat(matrix)
    except:
        print('输入错误，请重新输入')
        return mat(matrix_input())


def matrix_oper(matrix):
    func_n = eval(input('请输入功能对应的序号：'))
    if func_n == 1:
        print('请输入您要相加的矩阵')
        matrix_a = matrix_input()
        matrix_b = matrix + matrix_a
        print('相加之后的矩阵为：{}'.format(matrix_b))
    elif func_n == 2:
        print('请输入您要相减的矩阵')
        matrix_a = matrix_input()
        matrix_b = matrix - matrix_a
        print('相减之后的矩阵为：{}'.format(matrix_b))
    elif func_n == 3:
        digit = eval(input('请输入您要相乘的数字'))
        matrix_a = matrix * digit
        print('数乘之后的矩阵为：{}'.format(matrix_a))
    elif func_n == 4:
        print('请输入您要相乘的矩阵')
        matrix_a = matrix_input()
        matrix_b = matrix * matrix_a
        print('矩阵与矩阵相乘之后的矩阵为：{}'.format(matrix_b))
    elif func_n == 5:
        matrix_a = matrix.T
        print('其转置矩阵为：\n{}'.format(matrix_a))
    elif func_n == 6:
        matrix_a = matrix.I
        print('其逆矩阵为：\n{}'.format(matrix_a))
    elif func_n == 7:
        definite = linalg.eig(matrix)[0]
        print('矩阵的特征值为：', end=' ')
        for i in range(len(definite)):
            print('{:.2f}'.format(definite[i]), end=' ')
        print()
    elif func_n == 8:
        det_value = linalg.det(matrix)
        print('该行列式的值为：{:.2f}'.format(det_value))
    else:
        print('输入值有误')


def main():
    """
        主函数
    """
    print('请输入您要操作的矩阵')
    matrix = matrix_input()
    print(matrix)
    func_list = ['矩阵的相加', '矩阵的相减', '矩阵的数乘运算', '矩阵与矩阵的乘法运算', '求矩阵的转置矩阵',
                 '求矩阵的逆矩阵', '判断矩阵的特征值', '方阵的行列式计算']
    print('能实现的功能有：')
    for i in range(len(func_list)):
        print('{}：{}'.format(i + 1, func_list[i]))
    while True:
        matrix_oper(matrix)
        on = input('是否继续进行操作（Y/N）：')
        if on in ['N', 'n']:
            break
        else:
            change = input('是否需要更改操作的矩阵（Y/N）：')
            if change in ['Y', 'y']:
                matrix = matrix_input()
    print('操作结束')


if __name__ == '__main__':
    main()
