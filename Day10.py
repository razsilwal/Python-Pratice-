# Linear Transformation 

import numpy as np 

# A = np.array([[2,-1],
#               [3,4]])

# x= np.array([1,2])

# Tx = A @ x

# print("Vector: ", x)
# print("Transformed vector: ", Tx)



# Scaling in Linear Transformation

# kx, ky = 1.5, 0.5

# A = np.array([[kx, 0],
#              [0, ky]])

# x = np.array([2, 3])
# Sx = A @ x

# print("Original Vector: ", x)
# print("Scaling Vector: ", Sx)


# Rotation

# theta = np.pi / 2 # 90 degree 

# R = np.array([[np.cos(theta), -np.sin(theta)],
#               [np.sin(theta), np.cos(theta)]]) # CLOCKWISE ROTATE

# R1 = np.array([[np.cos(-theta), -np.sin(-theta)],
#               [np.sin(-theta), np.cos(-theta)]]) # ANTICLOCKWISE ROTATE

# v = np.array([2,3])

# Rv = R @ v
# Rv1 = R1 @ v
# print("Vector: ",v)
# print("Rotate Vector clockwise: ", Rv)
# print("Rotate Vector Anticlockwise: ", Rv1)



# Reflection 

# Rx = np.array([[1, 0],
#               [0, -1]]) # reflection along x axis
# Ry = np.array([[-1, 0],
#               [0, 1]]) # reflection along y axis

# x = np.array([4, 5])

# reflected_vector = Rx @ x
# reflected_vector1 = Ry @ x

# print("Original Vector:", x)
# print("Reflected Vector on x-axis:", reflected_vector)
# print("Reflected Vector on y-axis:", reflected_vector1)


# Composition of Linear Transformation 

A = np.array([[2, 3],
              [4, 9]])
B = np.array([[4, 7],
            [4, 10]])

x = np.array([1, 2])

result = B @ (A @ x)

intermediate_matrix = B @ A
result2 = intermediate_matrix @ x

print(result)
print(result2)