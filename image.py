# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 00:43:45 2019

@author: Haroon Traders
"""
from PIL import Image as im
from matplotlib import pyplot as plt
import numpy as np
import os
def filecount(root):
    fcount=len([x for x in os.scandir(root)])
    print(fcount)
    pat=list(str([]))
    for dirname,subdirlist,filelist in os.walk(root):
        print("name of directory : "+dirname)
        for fname in filelist:
            #print(fname)
            p=os.path.abspath(dirname+'/'+fname)
            pat.append(p)
    pat.pop(0)
    pat.pop(0)
    print(pat)
    return pat
def resize(arr_pic):
    size=200,200
    g=list([])
    for i in range(0,20):
        n=im.open(arr_pic[i])
        ii=plt.imread(arr_pic[i])
        img = im.fromarray(ii, 'RGB')
        d=img.resize(size)
        print(d)
        g.append(d)
    return g
num_py=np.zeros((20,200,200,3))
def main(arr):
    dire="photos"
    pp=filecount(dire)
    res=resize(pp)
    #print(type(res))
    #print(len(res))
    #print(res)
    print(type(arr))
    print(arr.ndim)
    print(arr.shape)
    for a in range(0,20):
        arr[a,:,:]=res[a]
    print(arr.shape)
    return arr
b=main(num_py)
print(b)
if __name__ == "__main__":
    main(num_py)