import numpy as np
import random

t1 = np.array([1, 2, 3])
print(t1)
print(t1.dtype)

t2 = np.array(range(1, 6))
print(t2)
print(t2.dtype)

t3 = np.arange(1, 6)
print(t3)

t4 = np.array([1, 0, 1, 0], dtype=bool)
print(t4)

t5 = t4.astype(np.int8)
print(t5)

t6 = np.array([random.random() for x in range(10)])
print(t6)

t7 = np.round(t6, 2)
print(t7)
