import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

X = np.arange(0,6 , 0.1)
Y = np.sin(X)

plt.plot(X,Y)
plt.show()

y1 = np.sin(X)
y2 = np.cos(X)

plt.plot(X,y1,label="sin")
plt.plot(X,y2,linestyle="--" , label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend()
plt.show()


img = imread('img.png')
plt.imshow(img)
plt.show()
