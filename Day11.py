import numpy as np

# v1 = np.array([1,0,0])
# v2 = np.array([0,1,0])
# v3 = np.array([0,0,1])

# v1 = np.array([1,0,0])
# v2 = np.array([0,1,0])
# v3 = np.array([1,1,0])

# A = np.column_stack((v1,v2,v3))

# Rank = np.linalg.matrix_rank(A)

# print(A)
# print(f"Rank of the matrix = {Rank}")




v1 = np.array([1,2])
v2 = np.array([2,4])
v3 = np.array([4,8])


A = np.column_stack((v1,v2,v3))

Rank = np.linalg.matrix_rank(A)

print(A)
print("Rank of matrix: ", Rank)