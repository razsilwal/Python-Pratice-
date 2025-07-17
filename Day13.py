import numpy as np 

# arr = np.array([1,2,3,4,5,6,7,8,9,10])
# re_array = arr.reshape(5,2)
# back = re_array.reshape(10)
# print("Original Array: ", arr)
# print("Reshaped Array(5,2): ",re_array)
# print("Back: ", back)


# arr_id = np.array([10,20,30,40])

# for num in arr_id:
#     print(num, end=" ")


# arr_2d = np.array([[10,20,30],[40,50,60]])

# for ls in arr_2d:
#     print(ls)
#     for num in ls:
#         print(num)

# for num in np.nditer(arr_2d): # it print 2d array all data in single 
#     print(num)


# a = np.array([1,2,3,4])
# b = np.array([5,6,7,8])

# add = a + b
# sub = a - b
# pro = a * b
# div = a / b
# exp = b ** 5
# re = b%a
# print("Sum of two array = ", add)
# print("Subtract of two array = ", sub)
# print("product of two array = ", pro)
# print("Division of two array = ", div)
# print(f"Power of each element {b} = {exp}")
# print(f"remainder of {b} % {a} = {re}")



# arr1 = np.arange(1,11)
# print(arr1)
# print("Square root = ", np.sqrt(arr1))
# print("Exponential (e^x) = ", np.exp(arr1))
# print("Sin = ", np.sin(arr1))
# print("cos = ", np.cos(arr1))
# print("tan = ", np.tan(arr1))
# print("natural log = ",np.log(arr1))
# print("log base 10 = ", np.log10(arr1))


# Statistical Functions 

# data = np.array([10, 20, 30, 40, 50])
# me = np.mean(data)
# md = np.median(data)
# sd = np.std(data)
# v = np.var(data)
# mini = np.min(data)
# maxi = np.max(data)

# print(f"Mean: {me}")
# print("Median: ",md)
# print("Standard Deviation: ", sd)
# print("Variance: ", v)
# print("Minimum: ", mini)
# print("maximum: ", maxi)
# print("Minimum value index =",np.argmin(data))
# print("Maximum value index =",np.argmax(data))


# A = np.array([[1,2],[3,4]])
# B = np.array([[200,6],[7,50]])

# determinant1 = np.linalg.det(A)
# determinant2 = np.linalg.det(B)

# inverse1 = np.linalg.inv(A)
# inverse2 = np.linalg.inv(B)

# print("Matrix A =", A)
# print("Matrix B =", B)
# print("Determinant of matrix A = ", determinant1)
# print("Determinant of matrix B = ", determinant2)
# print("Inverse of matrix A = ", inverse1)
# print("Inverse of matrix B = ", inverse2)


# Advanced Mathematical Functions

# arr = np.array([100, 200, 300, 400, 500])
# s = np.sum(arr)
# print("Original array =", arr)
# print("Sum of array =", s)
# cum_sum = np.cumsum(arr)
# print("Cumulative sum =", cum_sum)



# finidng unique elements and counting occurance

# arr = np.array([1,2,3,1,2,3,4,4,4])
# uni_arr, count = np.unique(arr, return_counts= True)
# print("unique value: ",uni_arr)
# print("Count : ",count)



# Sorting array 

# arr = np.array([3,1,4,1,5,9])
# print(f"Sorted array = {np.sort(arr)}")
# print(f"Index of sorted elements = {np.argsort(arr)}")
# print(f"Sorted array in descending = {np.sort(arr)[::-1]}")



# percentage and quartile

# data = np.array([10,20,30,40,50])
# print("25th Percentile or Q1 = ", np.percentile(data, 25)) 
# print("50th Percentile or Median = ", np.percentile(data, 50)) 
# print("75th Percentile or Q3 = ", np.percentile(data, 75))
# print("66th Percentile = ", np.percentile(data, 66))



