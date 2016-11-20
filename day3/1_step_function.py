import numpy as np
import matplotlib.pylab as plt

# define step function
def step_function(x):
    return (x>0).astype(np.int)

# using step function
print(step_function(np.array([-10,-6,2,4]))) # [0 0 1 1]

# show graph
x = np.arange(-10,10,0.1)
y = step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()

print("--------------")

# How to use NumPy
X = np.arange(-5,5,1)

## int list
## [-5 -4 -3 -2 -1  0  1  2  3  4]
print(X)

## -> bool list
## [False False False False False False  True  True  True  True]
print(X > 0) 

## -> int list (0 or 1)
## [0 0 0 0 0 0 1 1 1 1]
print((X > 0).astype(np.int))


