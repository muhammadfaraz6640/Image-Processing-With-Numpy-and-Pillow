# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:10:16 2019

@author: Haroon Traders
"""

'''from matplotlib import pyplot as plt
import numpy as np
im=plt.imread("C:/Users/Haroon Traders/Pictures/Picture1.jpg",1)
plt.imshow(im)
print(np.shape(im))
print(im)
im1=plt.imread("C:/Users/Haroon Traders/Pictures/untitled.png",1)
plt.imshow(im1)
print(np.shape(im1))
print(im1)
im1.reshape(200,200)
'''
from PIL import Image as im
from matplotlib import pyplot as plt
import numpy as np
size=200,200

#image1=im.open('C:/Users/Haroon Traders/Pictures/untitled.png')
#image1.show()
pics=list([])
for i in range(0,21):
   pics.append(f"C:/Users/Haroon Traders/Desktop/photos/{i+1}.png")
#a=im.open(pics[0])
#print(a.show())
#print(pics)
#abc=image1.resize(size)
#print(abc)
p=list([])
img=list([])
photos=np.zeros((20,200,200,3))
for a in range(0,20):
    p=im.open(pics[a])
    c=p.resize(size)
    #print(c)
    #c.show()
    plt.imsave(f"C:/Users/Haroon Traders/Desktop/resize/{a+1}.png",c)
    ab=plt.imread(f"C:/Users/Haroon Traders/Desktop/resize/{a+1}.png")
    img = im.fromarray(ab, 'RGB')
    photos[a,:,:,:]=img
    plt.imshow(photos[])
print(np.shape(img))
print(np.shape(photos))
print(photos)
