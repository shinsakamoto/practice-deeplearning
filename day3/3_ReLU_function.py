import numpy as np
import matplotlib.pylab as plt

# define relu_function function
def relu_function(x):
    return np.maximum(0,x)

# show graph
x = np.arange(-10,10,0.1)
y = relu_function(x)
plt.plot(x,y)
plt.ylim(-1.0,10)
plt.show()

print("--------------")

# How to use NumPy
X = np.arange(-5,5,1)

## [-5 -4 -3 -2 -1  0  1  2  3  4]
print(X)

## maximum
## [3 3 3 3 3 3 3 3 3 4]
print(np.maximum(3,X))


