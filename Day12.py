import numpy as np 

# arr_3d = np.array([[[2,3,5],[6,8,9]],[[3,4,7],[4,7,8]]])
# print(arr_3d)


# 3*3 matrix with all elements zero 

# zeros_a = np.zeros((3,3))
# print(zeros_a)

# 3*3 matrix with all elements one 

# one_a = np.ones((3,3,))
# print(one_a)


# to create an identitym matrix of size 5 * 5

# id_mat = np.eye(6)
# print(id_mat)

# we have to create array of first 50 numbers starting from 1

# arr = np.arange(1,51, 2)
# print(arr)


# we need an array having 5 values from 1 to 10 evenly spaced 
# sp_arr = np.linspace(1,10,5)
# print(sp_arr)


# this create a 4 x 4 matrix with all values ranging from 0 to 1
# random_arr = np.random.rand(4,4)
# print(random_arr)


# random_arr = np.random.randint(1,11, size=(4,4))
# print(random_arr)


# arr = np.array([[10, 20, 30],[20, 40, 70]])
# print(arr)
# print(f"No. of rows and columns : {arr.shape}")
# print(f"No. of elements = {arr.size}")
# print(f"Dimensional = {arr.ndim}")
# print(f"Data type = {arr.dtype}")
# print(f"Size occupied by item = {arr.itemsize}")
# print(f"space = {arr.nbytes}")



# arr_id = np.array([10,20,30,40,50])
# print(arr_id[::2])


# 
# arr_1d = np.array([10, 20, 30, 40, 50])
# print("First Element:", arr_1d[0]) # Access first element
# print("Last Element:", arr_1d[-1]) # Access last element
# print("Elements from index 1 to 3:", arr_1d[1:4]) # Slicing
# print("Every second element:", arr_1d[::2]) # Step slicing


arr_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(arr_2d)
print(arr_2d[2,2])
print("First Row",arr_2d[0,:])
print("Second Row:",arr_2d[2,:])
print("Print First and second column",arr_2d[:,0:2])
print("Print last column first and  last value",arr_2d[::2, 2])
print(arr_2d[0, ::2])
print(arr_2d[1,1:])
print("Print diagonal: ",arr_2d.diagonal())

anti_diag = np.fliplr(arr_2d).diagonal()
print("Anti Diagonal: ", anti_diag)