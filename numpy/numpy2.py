import numpy as np

# numpy calculation and function

array = np.random.randint(1,10,size = 4).reshape(2,2)
print(array)

result_array = array * 10
print(result_array)

# broadcasting (calculating different form of matrix)
array1 = np.arange(4).reshape(2,2) # 2*2
array2 = np.arange(2) # 1*2

array3 = array1 + array2
print(array3)

array4 = np.arange(0,8).reshape(2,4)
array5 = np.arange(0,8).reshape(2,4)
array6 = np.concatenate([array4,array5], axis=0)
array7 = np.arange(0,4).reshape(4,1) # 4 * 1
print(array6+array7)

# masking
array8 = np.arange(16).reshape(4, 4)
print(array8)
array9 = array8 < 10
print(array9)
array8[array9] = 100
print(array8)

array10 = np.arange(16).reshape(4, 4)
print(array10)
print("max: ", np.max(array10))
print("min: ", np.min(array10))
print("sum: ", np.sum(array10))
print("avg: ", np.mean(array10))

print("sum of each column: ", np.sum(array10, axis=0))
print("sum of each row: ", np.sum(array10, axis=1))
