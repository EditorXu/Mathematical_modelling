import numpy as np

# [[55, 24, 10], [65, 38, 22], [75, 40, 18], [100, 50, 20]]
#A = np.array(eval(input('请输入初始矩阵A=')))

print("请输入参评数目。")
n = eval(input())        #参评数目
print("请输入指标数目。")
m = eval(input())        #接收指标数目

# 接收用户输入的类型矩阵，该矩阵指示了每个指标的类型（极大型，极小型等）
print("请输入类型矩阵， 1：极大型， 2：极小型， 3：中间型， 4：区间型")
kind = input().split(" ")   # 将输入的字符串接空格分隔，形成列表

#接受用户输入的矩阵并转化为numpy数组
print("请输入矩阵。")
A = np.zeros(shape=(n, m)) #初始化一个n行m列的全零矩阵A
for i in range(n):
    A[i] = input().split(" ")           # 接收每行输入的数据
    A[i] = list(map(float, A[i]))       # 将接收到的字符串列表转换为浮点列表
print("请输入矩阵为：\n",format(A))        # 打印输入的矩阵A

def minTomax(maxx, x):
    x = list(x)                     # 将输入的指标数据转换为列表
    ans = [[maxx - e] for e in x]   # 计算最大值与每个指标值的差，并将其放入新列表中
    return np.array(ans)            # 将列表转换为numpy数组并返回

# 中间型指标转换为极大型指标的函数

def midTomax(bestx, x):
    x = list(x)                      # 将输入的指标数据转换为列表
    h = [abs(e - bestx) for e in x]  # 计算每个指标值与最优值之间的绝对差
    M = max(h)                       # 找到最大的差值
    if M == 0:
        M = 1                        # 防止最大差值为0的情况
    ans = [[(1-e/M)] for e in h]     # 计算每个差值占最大差值的比例，并从1中减去，得到新指标值
    return np.array(ans)             # 返回处理后的numpy数组

# 区间型指标转化为极大型指标的函数
def regTomax(lowx, highx, x):
    x = list(x)                                 # 将输入的指标数据转换为列表
    M = max(lowx-min(x), max(x)-highx)          # 计算指标值超出区间的最大距离
    if M == 0:
        M = 1                                   # 防止最大距离为0的情况
    ans = []
    for i in range(len(x)):
        if x[i] < lowx:
            ans.append([(1-(lowx-x[i])/M)])     # 如果指标值小于下限，则计算其与下限的距离比例
        elif x[i] > highx:
            ans.append([(1-(x[i]-highx)/M)])    # 如果指标值大于上限，则计算其与上限的距离比例
        else:
            ans.append([1])                     # 如果指标值在区间内，则直接取为1
    return np.array(ans)                        #  返回处理后的numpy数组

#  统一指标类型，将所有指标转化为极大型指标
X = np.zeros(shape=(n, 1))
for i in range(m):
    if kind[i]=="1":    # 如果当前指标为极大型，则直接使用原值
        v = np.array(A[:, i])
    elif kind[i]=="2":  # 如果当前指标为极小型，调用minTomax函数转化
        maxA = max(A[:, i])
        v = minTomax(maxA, A[:, i])
    elif kind[i]=="3":  # 如果当前指标为中间型，调用midTomax函数转化
        print("类型三，请输入最优值。")
        bestA = eval(input())
        v = midTomax(bestA, A[:, i])
    elif kind[i]=="4":  # 如果当前指标为区间型，调用regTomax函数转化
        print("类型四，请输入区间[a, b]值a。")
        lowA = eval(input())
        print("类型四，请输入区间[a, b]值b。")
        highA = eval(input())
        v = regTomax(lowA, highA, A[:, i])
    if i==0:
        X = v.reshape(-1, 1)    # 如果是第一个指标，直接替换X数组
    else:
        X = np.hstack([X, v.reshape(-1, 1)])    # 如果不是第一个指标，则将新指标列拼接到x数组上
print("统一指标后矩阵为。\n".format(X))    # 打印处理后的矩阵X

Mean = np.mean(X, axis=0)

Z = X / Mean

print('预处理后的矩阵为：')
print(Z)

Y = np.max(Z, axis=1)
X = Z

absX0_Xi = np.abs(X - np.tile(Y.reshape(-1, 1), (1, X.shape[1])))

a = np.min(absX0_Xi)
b = np.max(absX0_Xi)

rho = 0.5

gamma = (a + rho * b) / (absX0_Xi + rho * b)
weight = np.mean(gamma, axis=0) / np.sum(np.mean(gamma, axis=0))
score = np.sum(X * np.tile(weight, (X.shape[0], 1)), axis=1)
stand_S = score / np.sum(score)
sorted_S = np.sort(stand_S)[::-1]
index = np.argsort(stand_S)[::-1]

print('子序列中各项指标的灰色关联分别为')
print(np.mean(gamma, axis=0))

print('归一化后的得分及其索引（降序）')
print(sorted_S)
print(index)
