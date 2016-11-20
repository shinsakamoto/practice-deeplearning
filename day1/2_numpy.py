import numpy as np

x = np.array([1.0,2.0,3.0])
y = np.array([2.0,4.0,6.0])

print("-------------------------")

print(x) # [ 1.  2.  3.]
print(type(x)) # <class 'numpy.ndarray'>

print (x + y) # [ 3.  6.  9.]
print (x - y) # [-1. -2. -3.]
print (x * y) # [  2.   8.  18.]
print (x / y) # [ 0.5  0.5  0.5]
print (x ** y) # [   1.   16.  729.]

print (x + 1.0) # [ 2.  3.  4.]
print (x - 1.0) # [ 0.  1.  2.]
print (x * 3.0) # [ 3.  6.  9.]
print (x / 3.0) # [ 0.33333333  0.66666667  1.        ]
print (x ** 3.0) # [  1.   8.  27.]

x1 = np.array([1.0,2.0])
x2 = np.array([3.0,4.0,5.0])
# x1 + x2
# ValueError: operands could not be broadcast together with shapes (2,) (3,)

print("-------------------------")

A = np.array([[1,2],[3,4]])
B = np.array([[3,0],[0,6]])
C = np.array([2,3])

print(A)
# [[1 2]
#  [3 4]]
print(A.shape) # (2, 2)
print(A.dtype) # int64
print(A[0]) # [1 2]
print(A[0][0]) # 1
print(A[0][1]) # 2
print(A[1][0]) # 3
print(A[1][1]) # 4

for row in A:
    print(row)
# [1 2]
# [3 4]

print(B)
# [[3 0]
#  [0 6]]

print( A * B ) 
# [[ 3  0]
#  [ 0 24]]

print( A * 10 )
# [[10 20]
#  [30 40]]

print( A * C )
# [[ 2  6]
#  [ 6 12]]


print("-------------------------")

X = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(X)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(X.shape) # (3, 3)

Xflatten = X.flatten()
print(type(Xflatten)) # <class 'numpy.ndarray'>
print(Xflatten) # [1 2 3 4 5 6 7 8 9]

Xvalues = Xflatten[np.array([0,2,5])] # index no
print(type(Xvalues)) # <class 'numpy.ndarray'>
print(Xvalues) # [1 3 6]

print( Xflatten > 5 ) # [False False False False False  True  True  True  True]
print( Xflatten[Xflatten > 5] ) # [6 7 8 9]

