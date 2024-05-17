# # 一致性检验
# import numpy as np
# # numpy Pandas matplotlib
#
# A = np.array([[1, 2, 3, 5], [1/2, 1, 1/2, 2], [1/3, 2, 1, 2], [1/5, 1/2, 1/2, 1]])
#
# n = A.shape[0] #获取A的行，0变为1则是获取A的列， shape是获取形状信息
#
# eig_val,eig_vec = np.linalg.eig(A) #eig_val是特征值，eig_vec是特征向量
#
# Max_eig = max(eig_val) #求特征值的最大值
#
# CI = (Max_eig - n) / (n - 1)
# RI = [0, 0.001, 0.52, 0.89, 1.12, 1.26, 1.36, 1.41, 1.46, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59]
#
# CR = CI / RI[n-1]
#
# print('一致性指标CI=',CI)
# print('一致性比例CR=',CR)
#
# if CR < 0.10:
#     print('因为CR < 0.10，所以该判断矩阵A的一致性可以接受')
# else:
#     print('注意：CR >= 0.10, 因为该判断矩阵A需要进行修改')

# #算数平均法求权重
# import numpy as np
#
# A = np.array([[1, 2, 3, 5], [1/2, 1, 1/2, 2], [1/3, 2, 1, 2], [1/5, 1/2, 1/2, 1]])
#
# ASum = np.sum(A,axis=0)
#
# n = A.shape[0]
#
# Stand_A = A / ASum
#
# ASumr = np.sum(Stand_A, axis=1)
#
# weights = ASumr / n
#
# print(weights)

# # 几何平均法求权重
# import numpy as np
#
# A = np.array([[1, 2, 3, 5], [1/2, 1, 1/2, 2], [1/3, 2, 1, 2], [1/5, 1/2, 1/2, 1]])
#
# n = A.shape[0]
#
# prod_A = np.prod(A, axis=1)
#
# prod_n_A = np.power(prod_A, 1/n)
#
# re_prod_A = prod_n_A / np.sum(prod_n_A)
#
# print(re_prod_A)

# 特征值法求权重
import numpy as np

A = np.array([[1, 2, 3, 5], [1/2, 1, 1/2, 2], [1/3, 2, 1, 2], [1/5, 1/2, 1/2, 1]])

n = A.shape[0]

eig_values, eig_vectors = np.linalg.eig(A)

max_index = np.argmax(eig_values)

max_vectors = eig_vectors[:, max_index]

weights = max_vectors / np.sum(max_vectors)

print(weights)