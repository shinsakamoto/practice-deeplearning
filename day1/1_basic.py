x = 'hello world'
y = 123
z = 1.5
a = [1,2,3,4,5,]
b = True
c = False

print(type(x)) # <class 'str'>
print(type(y)) # <class 'int'>
print(type(z)) # <class 'float'>
print(type(a)) # <class 'list'>
print(type(b)) # <class 'bool'>

print(x) # hello world
print(y) # 123
print(z) # 1.5
print(a) # [1, 2, 3, 4, 5]
print(b) # True
print(not b) # False
print(b and c) # False
print(b or c) # True

# print function
## hello world!\n
print("hello world", end="")
print("!")
## a,b,c\n
print("a" , "b" , "c", sep=",")
## different type
print('string=' + x + ' int=' + str(y) ) # string=hello world int=123
## print('string=' + x + ' int=' + y) # TypeError: Can't convert 'int' object to str implicitly

print(1 + 1 + 1) # 3
print(1 - 2) # 1
print(3 * 4) # 12
print(7 / 5) # 1.4
print(2 ** 3) # 8

# syntax
## if-elif-else syntax
if a:
    print("a is true.")
elif b:
    print("a is false and b is true.")
else:
    print("other case")

## no swtch case syntax

## for syntax
# 0
# 1
# 2
for i in [0,1,2]:
    print(i)

# Function
def hello(obj):
    print("def hello() -> hello " + str(obj) + "!")
hello("world") # def hello() -> hello world!
hello(123) # def hello() -> hello 123!

# class
class Node:
    def __init__(self,name="no name",x=0,y=0,width=0,height=0):
        self.name = name
        self.setPosition(x,y)
        self.setSize(width,height)
    def setSize(self,width,height):
        self.width = width
        self.height = height
    def setPosition(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "<{0}> name={1} x,y=({2},{3}) width,height=({4},{5})".format( self.__class__.__name__ , self.name,self.x,self.y,self.width,self.height)
node1 = Node()
node2 = Node(x=10,y=20,width=100,height=80,name="node1")
print("initialized: {node}".format(node=node1)) # initialized: <Node> name=no name x,y=(0,0) width,height=(0,0)
print("initialized: {node}".format(node=node2)) # initialized: <Node> name=node1 x,y=(10,20) width,height=(100,80)


