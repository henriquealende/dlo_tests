import numpy as np


a = np.empty((4,4))

x = [1,3,4,5]
y = [9, 3 ,2, 1]

a[0,0:4] = x
a[1,0:4] = y

print(a)