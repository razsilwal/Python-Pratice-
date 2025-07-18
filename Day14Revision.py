import numpy as np 

# v = np.array([1, 2, 3])
# print(v)

mat = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
mat2 = np.array([[5,7,8],
                 [8,5,7],
                 [7,3,4]])

# new_mat = 5 * mat
# print(new_mat)

# add_mat = mat + mat2 # it adds 2 matrix
# sub_mat = mat2 - mat
# print(add_mat)
# print(sub_mat)

# t_mat1 = mat.T # it help to transpose the matrix 
# t_mat2 = mat2.T
# print(t_mat1)
# print(t_mat2)

# null_mat = mat @ mat2  # it helps to do dot product 
# print(null_mat)

# det1 = np.linalg.det(mat) # it helps to find deteminant 
# det2 = np.linalg.det(mat2)
# print(det1)
# print(det2)

# inv_mat1 = np.linalg.inv(mat)
# inv_mat2 = np.linalg.inv(mat2)
# print(inv_mat1)
# print(inv_mat2)


# 2x + 3y = 8 
# 5x + 4y = 13

# A = np.array([[2,3],[5,4]])
# b = np.array([8,13])
# cal = np.linalg.solve(A, b) 
# print(cal)


# A = np.array([[8,3,-2],
#               [-4,7,5],
#               [3,4,-12]])
# b = np.array([9,15,35])
# cal = np.linalg.solve(A, b)
# print(cal)

# import scipy.linalg as la 

# A= np.array([[2,4,5],
#              [1,6,2],
#              [4,2,1]])

# P,L,U = la.lu(A)
# print(P)
# print(L)
# print(U)

kx, ky = 2,5
A = np.array([[kx, 0],
             [0,ky]])
x = np.array([4,5])

t_s = A @ x
print(x)
print(t_s)