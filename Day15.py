import numpy as np


#Broadcasting 

# arr = np.array([1,2,3,4,5])
# s = 5

# new_arr = arr * 5
# print(arr)
# print(new_arr)


# s = 4

# mat = np.array([[1,2,4],
#                 [2,3,5],
#                 [5,7,3]])

# new_mat = mat - s
# new_mat2 = s - mat
# print(mat)
# print(new_mat) 
# print(new_mat2) 

# mat = np.array([[2,4,7],
#                 [3,4,6],
#                 [4,6,9]])

# v = np.array([1,2,3])
# new_mat = mat + v
# print(mat)
# print(new_mat)

# 1D
# a = np.array([1,8,5,6,4,2])
# print(np.sort(a))


# m = np.array([[9,6,4],
#               [2,1,8],
#               [7,9,1]])
# new_row = np.sort(m, axis=1) # it helps to sort the value of each row 
# new_col = np.sort(m, axis=0) # it helps to sort the value of matrix in column
# print(m)
# print(new_row)
# print(new_col)



mat = np.array([[1,2,3],
                [2,3,6]])
new_row = np.array([[2,5,7]])
new_row2 = np.array([[3],
                     [4],
                     [6]])

new_mat = np.append(mat, new_row, axis=0)

new_mat2 = np.append(new_mat, new_row2, axis=1)
print(mat)
print(new_mat)
print(new_mat2)


# mat = np.array([[1,2,3],
#                 [2,3,6]])

# new_col = np.array([[1],
#                     [2]])
# new_mat = np.append(mat, new_col, axis=1)

# print(new_mat)




