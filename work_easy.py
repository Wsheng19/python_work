"""
    python简单作业
    功能：实现矩阵的一些小应用
"""


# 矩阵的输入
def matrix_input():
    try:
        err = 0
        matrix = []
        row, column = eval(input('请依次输入矩阵的行和列(中间用英文逗号隔开)'))
        print('请逐行输入矩阵的数据（元素之间用逗号隔开，输完一行元素按一下回车）')
        for i in range(row):
            list_1 = []
            if column != 1:
                tup = eval(input())
                list_1 = list(tup)
            elif column == 1:
                list_1.append(eval(input()))
            if len(list_1) == column:
                matrix.append(list_1)
            elif len(list_1) != 0:
                print('输入错误,请重新输入')
                err = 1
                break
        if err:
            return matrix_input()
        else:
            return matrix
    except:
        print('输入错误，请重新输入')
        return matrix_input()


# 判断矩阵是否为方阵
def Is_square(matrix):
    if len(matrix) == len(matrix[0]):
        return True
    else:
        return False


# 方阵的行列式计算
def matrix_det(matrix):
    if Is_square(matrix):
        det_value = 0
        if len(matrix) == 0:
            return det_value
        elif len(matrix) == 1:
            det_value = matrix[0][0]
        else:
            matrix_a = []
            for p in range(len(matrix)):
                matrix_a.append(matrix[p][:])
            for i in range(len(matrix[0])):
                current = matrix[0][i]
                matrix_b = []
                for k in range(len(matrix)):
                    matrix_b.append(matrix[k][:])
                matrix_b.pop(0)
                for j in range(len(matrix_b)):
                    matrix_b[j].pop(i)
                det_value += pow(-1, i) * current * matrix_det(matrix_b[:])
                matrix = matrix_a
        return det_value
    else:
        return '该矩阵不是方阵，无法计算该矩阵行列式的值'


# 判断方阵是否为可逆矩阵
def Is_reversible(matrix):
    if Is_square(matrix):
        if matrix_det(matrix):
            return True
    else:
        return False


# 矩阵的输出
def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()


# 矩阵的相加
def matrix_add(matrix_a, matrix_b):
    if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
        matrix = []
        for i in range(len(matrix_a)):
            list_1 = []
            for j in range(len(matrix_a[0])):
                list_1.append(matrix_a[i][j] + matrix_b[i][j])
            matrix.append(list_1)
        return matrix
    else:
        print('这两个行列式不能相加')
        return []


# 矩阵的相减
def matrix_minus(matrix_a, matrix_b):
    if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
        matrix = []
        for i in range(len(matrix_a)):
            list_1 = []
            for j in range(len(matrix_a[0])):
                list_1.append(matrix_a[i][j] - matrix_b[i][j])
            matrix.append(list_1)
        return matrix
    else:
        print('这两个行列式不能相减')
        return []


# 矩阵的数乘运算
def matrix_digit_mul(matrix, digit):
    matrix_a = []
    for i in range(len(matrix)):
        list_1 = []
        for j in range(len(matrix[0])):
            list_1.append(matrix[i][j] * digit)
        matrix_a.append(list_1)
    return matrix_a


# 矩阵与矩阵的乘法运算
def matrix_double_mul(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        print('这两个矩阵不能相乘')
        return []
    else:
        matrix_c = []
        for i in range(len(matrix_a)):
            list_1 = []
            for j in range(len(matrix_b[0])):
                c = 0
                for k in range(len(matrix_a[0])):
                    c += matrix_a[i][k] * matrix_b[k][j]
                list_1.append(c)
            matrix_c.append(list_1)
        return matrix_c


# 求矩阵的转置矩阵
def matrix_trans(matrix):
    matrix_a = []
    for i in range(len(matrix[0])):
        list_1 = []
        for j in range(len(matrix)):
            list_1.append(matrix[j][i])
        matrix_a.append(list_1)
    return matrix_a


# 求矩阵的伴随矩阵
def matrix_adjoint(matrix):
    if Is_square(matrix):
        adjoint = []
        for i in range(len(matrix[0])):
            list_1 = []
            for j in range(len(matrix)):
                matrix_a = []
                for k in range(len(matrix)):
                    matrix_a.append(matrix[k][:])
                matrix_a.pop(j)
                for p in range(len(matrix_a)):
                    matrix_a[p].pop(i)
                value = pow(-1, i + j) * matrix_det(matrix_a)
                list_1.append(value)
            adjoint.append(list_1)
        return adjoint
    else:
        return []


# 求矩阵的逆矩阵
def matrix_inverse(matrix):
    if Is_reversible(matrix):
        matrix_a = matrix_adjoint(matrix)
        matrix_b = matrix_digit_mul(matrix_a, pow(matrix_det(matrix), -1))
        return matrix_b
    else:
        return ['该矩阵没有逆矩阵']


# 判断矩阵的定
def matrix_definite(matrix):
    definite = []
    if Is_square(matrix):
        flag = []
        for i in range(len(matrix)):
            matrix_a = []
            for j in range(0, i + 1):
                list_1 = []
                for k in range(i + 1):
                    list_1.append(matrix[j][k])
                matrix_a.append(list_1)
            value = matrix_det(matrix_a)
            if value > 0:
                flag.append(1)
            elif value == 0:
                flag.append(0)
            else:
                flag.append(-1)
        # 判断是否为正定
        for n in range(len(matrix)):
            if flag[n] != 1:
                definite.append('非正定')
                break
            if n == len(matrix) - 1:
                definite.append('正定')
        # 判断是否为负定
        for m in range(len(matrix)):
            if m % 2 == 0:
                if flag[m] != -1:
                    definite.append('非负定')
                    break
            elif m % 2 == 1:
                if flag[m] != 1:
                    definite.append('非负定')
                    break
            if m == len(matrix) - 1:
                definite.append('负定')
        return definite
    else:
        print('该矩阵不是方阵')
        return definite


def matrix_oper(matrix):
    func_n = eval(input('请输入功能对应的序号：'))
    if func_n == 1:
        print('请输入您要相加的矩阵')
        matrix_a = matrix_input()
        matrix_b = matrix_add(matrix, matrix_a)
        print('相加之后的矩阵为：')
        matrix_print(matrix_b)
    elif func_n == 2:
        print('请输入您要相减的矩阵')
        matrix_a = matrix_input()
        matrix_b = matrix_minus(matrix, matrix_a)
        print('相减之后的矩阵为：')
        matrix_print(matrix_b)
    elif func_n == 3:
        digit = eval(input('请输入您要相乘的数字'))
        matrix_a = matrix_digit_mul(matrix, digit)
        print('数乘之后的矩阵为：')
        matrix_print(matrix_a)
    elif func_n == 4:
        print('请输入您要相乘的矩阵')
        matrix_a = matrix_input()
        matrix_b = matrix_double_mul(matrix, matrix_a)
        print('矩阵与矩阵相乘之后的矩阵为：')
        matrix_print(matrix_b)
    elif func_n == 5:
        matrix_a = matrix_trans(matrix)
        print('其转置矩阵为：')
        matrix_print(matrix_a)
    elif func_n == 6:
        matrix_a = matrix_inverse(matrix)
        print('其逆矩阵为：')
        matrix_print(matrix_a)
    elif func_n == 7:
        definite = matrix_definite(matrix)
        print('矩阵的定为：{}'.format(definite))
    elif func_n == 8:
        det_value = matrix_det(matrix)
        print('该行列式的值为：{}'.format(det_value))
    elif func_n == 9:
        print('该矩阵的伴随矩阵为：')
        matrix_a = matrix_adjoint(matrix)
        matrix_print(matrix_a)
    else:
        print('序号输入错误')


def main():
    """
        主函数
    """
    print('请输入您要操作的矩阵')
    matrix = matrix_input()
    print('您要操作的矩阵为：')
    matrix_print(matrix)
    func_list = ['矩阵的相加', '矩阵的相减', '矩阵的数乘运算', '矩阵与矩阵的乘法运算', '求矩阵的转置矩阵',
                 '求矩阵的逆矩阵', '判断矩阵的定', '方阵的行列式计算', '方阵的伴随矩阵']
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
