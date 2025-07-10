import numpy as np
import scipy.linalg as la



# # vector 
# v = np.array([1,2,3])
# print(v)


# matrix
# A = np.array([[1,2],[3,4]])
# print(A) 


# Scaler Multiplication
# v_scaled = 10 * v
# print(v_scaled)



A = np.array([[1,2],[3,4]])
B = np.array([[2,4],[6,8]])
# B = np.array([2,4])
# C = A @ B # it helps to find the matrix multiplication

# print(f"{A} x {B} = {C}")

# add_v = A+B
# print(f"{A} + {B} = {add_v}") 

# transpose 
# a_transpose = A.T
# print(a_transpose)


# 2x + 3y = 8
# 5x + 4y = 13

# a = np.array([[2,3],[5,4]])
# b = np.array([8,13])
# c = np.linalg.solve(a,b)
# print(f"Solution: {c}")


# a = np.array([[8,3,-2],[-4,7,5],[3,4,-12]])
# b = np.array([9,15,35])
# c = np.linalg.solve(a,b)
# print(f"Solution: {c}")



# A = ([[2,4,5],
#       [1,3,2],
#       [4,2,1]])

# P, L, U = la.lu(A)
# print(f"P = {P}")
# print(f"L = {L}")
# print(f"U = {U}")

A1 = np.array([[2, 4, 5],
              [1 ,3 ,2],
              [4, 2, 1]])

P, L, U = la.lu(A1) # [p, l, u]
# print(P)
# print(L)
# print(U)
f_val = P @ A1
l_val = L @ U
print(f_val)
print(l_val)


# A = QR
A = np.array([[1,2,3],
              [3,4,5]])
Q,R = np.linalg.qr(A)
result = Q @ R
print(A)
print(result)
