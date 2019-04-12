import numpy as np

t1 = np.array([[3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9]])
print(t1.shape)

print(t1.flatten())

t2 = t1.reshape(3, 4)
print(t2)
print(t2 + 2)

t3 = t2.reshape(2, 2, 3)
print(t3)

t4 = np.array([[6, 7, 8], [7, 8, 9]])
print(t3 + t4)
print('---------------')
t5 = np.array([[2, 2, 2], [3, 3, 3]])
print(t4 * t5)
