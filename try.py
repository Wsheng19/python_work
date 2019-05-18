import random
import time
#
# for i in range(12):
#     print(chr(9800 + i), end=' ')
# print('{}, {}, {}'.format(ord('徐'), ord('伟'), ord('盛')))
#
# for i in range(12):
#     print(random.randint(1, 6))
#
# a = 3
# b = 2
# print(a if a > b else b)
#
#
# class Person:
#     name = '小明'
#
#
# p1 = Person()
# p2 = Person()
# p1.name = '小红'
#
# print(p1.name)
# print(p2.name)
# print(Person.name)
#
# s = input()
# str_list = s.split('-')
# print('{}+{}'.format(str_list[0], str_list[-1]))
# flag = 1
# Sum = 0
# start = time.perf_counter()
# for i in range(2, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             flag = 0
#             break
#     if flag == 1:
#         Sum += i
#     flag = 1
# End = time.perf_counter()
# print(Sum)
# print(End - start)
# 生成随机密码
# import random
#
#
# def genpwd(length):
#     pd = random.randint(10**(length - 1), 10**length - 1)
#     return pd
#
#
# length = eval(input())
# random.seed(17)
# for i in range(3):
#     print(genpwd(length))
# 集合
# a = {2, 3, 4}
# b = set('123')
# c = a | b
# d = a - b
# e = a & b
# f = a ^ b
# print('{}{}{}{}'.format(c, d, e, f))
# a.add('xws')
# # a.discard(1)
# # a.remove(2)
# print(a)
# x = ['x', 'w', 's', 'x', 'w', 's', 'n', 'b']
# x = list(set(x))
# print(x)
# 列表
# a = [1, 2, 3]
# del a[0:2]
# print(a)
# b = a + []
# a += [1, 2]
# print(b)
# print(a)
a = [[1, 2], [3, 4]]
b = a + []
matrix_a = []
for k in range(len(a)):
    matrix_a.append(a[k][:])
a.pop()
print(matrix_a)
print(b)
b[0].pop()
print(a + [])
