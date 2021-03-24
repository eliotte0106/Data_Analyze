import numpy as np

#size,data type
list_data = [1,2,3]
array = np.array(list_data)
print(array.size)
print(array.dtype)

#0~3 matrix
array1 = np.arange(4)
print(array1)
array2= np.zeros((4,4),dtype=float)
print(array2)
array3 = np.ones((3,3),dtype=str)
print(array3)

#0~9 random matrix
array4 = np.random.randint(0,10,(3,3))
print(array4)

#avg = 0, standard diff = 1 matrix
array5 = np.random.normal(0,1,(3,3))
print(array5)

#array concatenate(horizontal)
array5 = np.array([1,2,3])
array6 = np.array([4,5,6])
array7 = np.concatenate([array5,array6])
print(array7.shape)
print(array7)

#changing matrix shape
array8 = np.array([1,2,3,4])
array9 = array8.reshape((2,2))
print(array9)

#matrix shape change(vertical)
array10 = np.arange(4).reshape(1,4)
array11 = np.arange(8).reshape(2,4)
print(array10)
print(array11)

#matrix concatenate(vertical)
array12 = np.concatenate([array10,array11], axis = 0)
print(array12)

#matrix divide

array13 = np.arange(8).reshape(2,4)
left, right = np.split(array13,[2],axis=1)
print(left.shape)
print(right.shape)
print(array13)
print(left)