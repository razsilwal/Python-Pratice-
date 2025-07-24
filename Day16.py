
import numpy as np 



# Orthogonality and projection 

# v1 = np.array([1,-1,3])
# v2 = np.array([2,2,3])

# proj = (np.dot(v1, v2) / np.dot(v2, v2)) * v2

# print(proj)


# M = np.array([[1,2,3],[3,4,5],[5,6,7]])
# c1, c2 = 1.5, 2

# l_c  = c1 * M[0] + c2 * M[2]
# print(l_c)


# v1 = np.array([1,2,3])
# v2 = np.array([2,5,6])
 
# M = np.stack([v1,v2], axis=1)
# print(M)
# r = np.linalg.matrix_rank(M)
# print(r)

# is_independent = (r == M.shape[1])
# if is_independent:
#     print("The vector are independent")
# else:
#     print("The Vectors are dependent")


from sklearn.decomposition import PCA

x = np.random.rand(5,3)

p = PCA(n_components = 2)

reduced = p.fit_transform(x)

print(reduced)