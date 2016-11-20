
# y = 0 (x1 * w1 + w2 + x2 * w2) <= theta
# y = 1 (x1 * w1 + w2 + x2 * w2) > theta
#
# x1,x2 : Input
# w1,w2 : Weight
# theta : threshold
# y : output
#
# AND
# x1 | x2 | y
# 0  | 0  | 0
# 1  | 0  | 0
# 0  | 1  | 0
# 1  | 1  | 1
# 
# x1 * w1 -> 
#             y -> 0 or 1
# x2 * w2 -> 

def AND(x1,x2):
    w1,w2,theta=0.5,0.5,0.7 # decide manually
    tmp = x1*w1+x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

print(AND(0,0)) # 0
print(AND(1,0)) # 0
print(AND(0,1)) # 0
print(AND(1,1)) # 1
