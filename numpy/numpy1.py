import numpy as np

# save and call a single object
array = np.arange(0,10)
np.save('saved.npy', array)
result = np.load('saved.npy')
print(result)

# save and call many objects

array1 = np.arange(0,10)
array2 = np.arange(10,20)
np.savez('saved.npz', array1=array1, array2=array2)

data = np.load('saved.npz')
result1 = data['array1']
result2 = data['array2']
print(result1)
print(result2)

# numpy ascending sort
array3 = np.array([5,9,10,3,1])
array3.sort()
print(array3)
print(array3[::-1]) # reversed

# sort by column
array4 = np.array([[5,9,10,3,1], [8,3,4,2,5]])
print(array4)
array4.sort(axis=0)
print(array4)

# data creation by space
array5 = np.linspace(0,10,5) # between 0 and 10 for 5 nums
print(array5)

# random number
# np.random.seed(7) #set
# print(np.random.randint(0,10(2,3)))

# numpy array copy
array6 = np.arange(0, 10)
array7 = array6.copy()
array7[0] = 99
print(array7)

# remove duplicates

array8 = np.array([1,1,2,2,2,3,3,4])
print(np.unique(array8))

