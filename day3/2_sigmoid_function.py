import numpy as np
import matplotlib.pylab as plt

# define sigmoid_function function
def sigmoid_function(x):
    return 1 / (1+np.exp(-x))

# show graph
x = np.arange(-10,10,0.1)
y = sigmoid_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()

print("--------------")

# How to use NumPy
X = np.arange(-5,5,1)

## int list
## [-5 -4 -3 -2 -1  0  1  2  3  4]
print(X)

## +1
## [-4 -3 -2 -1  0  1  2  3  4  5]
print(1 + X) 

## +1
## [-0.25 -0.333 -0.5 -1. inf  1. 0.5  0.333 0.25 0.2]
print( 1 / (1 + X) )


