"""
    汉诺塔
"""
count = 0


def hanoi(n, A, B, C):
    global count
    if n == 1:
        count += 1
        print('{}:{}->{}'.format(1, A, C))
    else:
        hanoi(n-1, A, C, B)
        print('{}:{}->{}'.format(n, A, C))
        count += 1
        hanoi(n-1, B, A, C)


hanoi(3, 'A', 'B', 'C')
print(count)
