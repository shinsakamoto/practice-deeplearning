import numpy as np

# y = 0 (x1 * w1 + w2 + x2 * w2) <= theta
# y = 1 (x1 * w1 + w2 + x2 * w2) > theta
#
# ->
#
# y = 0 ( b + x1 * w1 + w2 + x2 * w2) <= 0
# y = 1 ( b + x1 * w1 + w2 + x2 * w2) > 0
#
# x1,x2 : Input
# w1,w2 : Weight
# b : bias
# y : output
# 
# x1 * w1 -> 
#             y -> 0 or 1
# x2 * w2 -> 


# AND
# x1 | x2 | y
# 0  | 0  | 0
# 1  | 0  | 0
# 0  | 1  | 0
# 1  | 1  | 1

def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1
print("AND")
print(AND(0,0)) # 0
print(AND(1,0)) # 0
print(AND(0,1)) # 0
print(AND(1,1)) # 1


# NAND
# x1 | x2 | y
# 0  | 0  | 1
# 1  | 0  | 1
# 0  | 1  | 1
# 1  | 1  | 0

def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

print("NAND")
print(NAND(0,0)) # 1
print(NAND(1,0)) # 1
print(NAND(0,1)) # 1
print(NAND(1,1)) # 0

# OR
# x1 | x2 | y
# 0  | 0  | 0
# 1  | 0  | 1
# 0  | 1  | 1
# 1  | 1  | 1

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1
print("OR")
print(OR(0,0)) # 0
print(OR(1,0)) # 1
print(OR(0,1)) # 1
print(OR(1,1)) # 1


# XOR
# x1 | x2 | s1 | s2 | y
# 0  | 0  | 1  | 0  | 0
# 1  | 0  | 1  | 1  | 1
# 0  | 1  | 1  | 1  | 1
# 1  | 1  | 0  | 1  | 0

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

print("XOR")
print(XOR(0,0)) # 0
print(XOR(1,0)) # 1
print(XOR(0,1)) # 1
print(XOR(1,1)) # 1
