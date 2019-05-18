X = []

rows = eval(input("请输入第一个矩阵X的行数："))
columns = eval(input("请输入第一个矩阵X的列数："))

for row in range(rows):
    X.append([])
    for column in range(columns):
        num = eval(input("请按行顺序依次输入数字："))
        X[row].append(num)
        
print("你输入的第一个矩阵X是：")
print(X)

Y = []

rows = eval(input("请输入第二个矩阵Y的行数："))
columns = eval(input("请输入第二个矩阵Y的列数："))

for row in range(rows):
    Y.append([])
    for column in range(columns):
        num = eval(input("请再次按行顺序依次输入数字："))
        Y[row].append(num)
        
print("你输入的第二个矩阵Y是：")
print(Y)

    
Z = []

for row in range(rows):
    Z.append([])
    for column in range(columns):
        Z[row].append(0)

for i in range(rows):
    for j in range(columns):
        Z[i][j] = X[i][j] + Y[i][j]

print("两个矩阵的和X+Y是：")
print(Z)

W = []

for row in range(rows):
    W.append([])
    for column in range(columns):
        W[row].append(0)

for i in range(rows):
    for j in range(columns):
        W[i][j]=X[i][j]-Y[i][j]

print("两个矩阵的差X-Y是：")
print(W)
