## (1) 1 dimensional array out of list 
import numpy as np
ls = [12.23, 13.32, 100, 36.32]
array = np.array(ls)
print(array)                                                                                                                                               ###  (2) Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10
matrix = np.arange(2,11).reshape(3,3)
print("matrix of numbers between 2 & 10 is:"),
print(matrix )                                                                                                                                ### (3) create vector of 10 zeros and range the 6th value to 11:
vector_10d = np.zeros(10)
update = vector_10d[5] = 11
print(vector_10d)                                                                                                                                          ### (4) Write a NumPy program to create an array with values ranging from 12 to 38.
array1 = np.arange(12,38)
print(array1)                                                                                                                                                                             ### (5) Write a NumPy program to convert an array to a floating type.
ls = [1,2,3,4]
arr = np.array(ls)
fl = arr.astype(float)
print(f"floated array is: {fl}")                                                                                                                               ### (6) Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.
degree_c = np.array([32.0, 12.0, -8.0, 45.0])
def Centigrade_into_Fahrenheit(degree_c):
    converted_f = (9/5 * degree_c) + 32
    return converted_f
converted_f = Centigrade_into_Fahrenheit(degree_c)
print(converted_f)                                                                                                                                                           ### (7) Write a NumPy program to append values to the end of an array.
import numpy as np
arr = np.array([10,20,30,40])
def appending_values_into_array(arr):
    add = np.append(arr,50)
    return add 
add = appending_values_into_array(arr)
print(add)                                                                                                                                                                                                                                 ### (8) Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.
my_array = np.array([18,45,67,23,43,12,17,19,56,100])
mean = np.mean(my_array)
print(f"Mean of the array is {mean}")

median = np.median(my_array)
print(f"Median of the array is {median}")

standard_deviation= np.std(my_array)
print(f"tandard deviation of the array is {standard_deviation}")                                                       ### (9) Create a 10x10 array with random values and find the minimum and maximum values.
array = np.arange(1,101).reshape(10,10)
max = np.max(array)
print(f"Maximum vslue of tha array: {max}")
min = np.min(array)
print(f"Minimum vslue of tha array: {min}")                                                                                                    ### (10) 
random_array = np.arange(27).reshape(3,3,3)
print(random_array)
