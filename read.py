# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:15:08 2020

@author: William
"""

# +

import cv2
import os
# -



# import cv2

import csv
#import random
#import time
#import numpy as np
#import pandas as pd
#import matplotlib.image as mpimg # mpimg 用於讀取圖片
#import matplotlib.pyplot as plt # plt 用於顯示圖片
#import seaborn as sns
# 設定顯示中文字體
#from matplotlib.font_manager import FontProperties
#plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
# Keras深度學習模組套件

# tensorflow深度學習模組套件
# from tensorflow.keras import models
# from tensorflow.keras import layers
# import tensorflow.keras 
# from tensorflow import keras
# import tensorflow as tf

# +
#csvfile = open('AIMango/Sample_Label.csv')
csvfile = open('index_ggo.csv')

#csvfile = open('AIMango/dev.csv')
# -

reader = csv.reader(csvfile)




# 讀取csv標籤
labels = []
for line in reader:
#    tmp = [line[0],line[1]]
    # print tmp
    labels.append(line[0])

csvfile.close() 


picnum = len(labels)
print("圖片數量: ",picnum)


X = []

y = []
inline_labels = []
cnt=1
count=0
for filename in labels:
    csvfile = open("train/GGOLabel/"+filename+".txt")
    reader = csv.reader(csvfile)
    
    img=cv2.imread("train/GGOPNG/"+filename[:-3]+".png")    
    horizontal_img= cv2.flip(img,1)
    vertical_img= cv2.flip(img,0)
    
    write_txt=open("./darknet/1/"+filename+".txt",'w')
    i=0
    row=[]
    for line in reader:
        row.append(line)
        
    for line in row:
        if i%2==0 & i!=0:
            i+=1
            continue
        line2=row[i+1]
        print(line)
        print(line2)
    
    #1111111111111111111111111111111111111111111111111111111111111111111111111
    #inline_labels.append([str(count)+" "])
    #count+=1
    #inline_labels[-1].append("train/GGOPNG/"+filename[:-3]+".png ") #要改成絕對路徑
    
   
    w=img.shape[0]
    h=img.shape[1]
    
    #inline_labels[-1].append(str(w))
    #inline_labels[-1].append(" ")
    #inline_labels[-1].append(str(h))
    #inline_labels[-1].append(" ")
    '''
    for line in reader:
        print(line)
        if cnt!=1:
            inline_labels[-1].append(" ")
        if cnt%2!=0:
           
            inline_labels[-1].append(line[2])
            inline_labels[-1].append(" ")
            inline_labels[-1].append(line[0])
            inline_labels[-1].append(" ")
            inline_labels[-1].append(line[1])
        else:
            inline_labels[-1].append(line[0])
            inline_labels[-1].append(" ")
            inline_labels[-1].append(line[1])
        cnt+=1
    inline_labels[-1].append("\n")'''
    
    '''
    #22222222222222222222222222222222222222222222222222222222222222222222222
    csvfile = open("train/GGOLabel/"+filename+".txt")
    reader = csv.reader(csvfile)
    
    inline_labels.append([str(count)+" "])
    count+=1
    inline_labels[-1].append("train/GGOPNG/"+filename[:-3]+"_horizontal.png ") #要改成絕對路徑
    cv2.imwrite("train/GGOPNG/"+filename[:-3]+"_horizontal.png", horizontal_img)
    
   
   
    inline_labels[-1].append(str(w))
    inline_labels[-1].append(" ")
    inline_labels[-1].append(str(h))
    inline_labels[-1].append(" ")
    cnt=1
    for line in reader:
        if cnt!=1 and cnt%2!=0:
            inline_labels[-1].append(" ")
        if cnt%2!=0:
            x1=line[0]
            y1=line[1]
        else:
            inline_labels[-1].append(line[2])
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str(w-int(line[0]))) #x1
                                     
            inline_labels[-1].append(" ")
                                     
            inline_labels[-1].append(y1) #y1
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str(w-int(x1))) #x2
            inline_labels[-1].append(" ")
            inline_labels[-1].append(line[1]) #y2
        cnt+=1
    inline_labels[-1].append("\n")
    #********************************
    csvfile = open("train/GGOLabel/"+filename+".txt")
    reader = csv.reader(csvfile)
    inline_labels.append([str(count)+" "])
    count+=1
    inline_labels[-1].append("train/GGOPNG/"+filename[:-3]+"_vertical.png ") #要改成絕對路徑
    cv2.imwrite("train/GGOPNG/"+filename[:-3]+"_vertical.png", vertical_img)
    
   
    cnt=1
    inline_labels[-1].append(str(w))
    inline_labels[-1].append(" ")
    inline_labels[-1].append(str(h))
    inline_labels[-1].append(" ")
    for line in reader:
        if cnt!=1 and cnt%2!=0:
            inline_labels[-1].append(" ")
        if cnt%2!=0:
            x1=line[0]
            y1=line[1]
        else:
            inline_labels[-1].append(line[2])
            inline_labels[-1].append(" ")
            inline_labels[-1].append(x1) #x1
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str(h-int(line[1]))) #y1
            inline_labels[-1].append(" ")
            inline_labels[-1].append(line[0]) #x2
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str(h-int(y1))) #y2
        cnt+=1
    inline_labels[-1].append("\n")
    
    
    '''
    
    csvfile.close() 
    cnt=1
w_file = open("train.txt",mode='a')
for r in inline_labels:
    w_file.writelines(r)
w_file.close()

img=cv2.imread("train/GGOPNG/GGO000501.png")
print(img.shape)

y = []
inline_labels = []
cnt=1
count=0
for filename in labels:
    csvfile = open("train/GGOLabel/"+filename[:-4]+".txt")
    reader = csv.reader(csvfile)
    print("train/GGOPNG/"+filename)
    img=cv2.imread("train/GGOPNG/"+filename)    
    horizontal_img= cv2.flip(img,1)
    vertical_img= cv2.flip(img,0)
    
    
    inline_labels = []

    #1111111111111111111111111111111111111111111111111111111111111111111111111
    inline_labels.append([])
    count+=1
    #inline_labels[-1].append("train/GGOPNG/"+filename[:-3]+".png ") #要改成絕對路徑
    
   
    w=img.shape[0]
    h=img.shape[1]
    img_resize=cv2.resize(img,(416,416))
    cv2.imwrite("./1/train/"+filename, img_resize)
    for line in reader:
        #if cnt!=1:
         #   inline_labels[-1].append(" ")
        if cnt%2!=0:
           
            inline_labels[-1].append(str(line[2]))
            inline_labels[-1].append(" ")
            xmin = int(line[0])
            ymin = int(line[1])
        else:
            xmax = int(line[0])
            ymax = int(line[1])
            inline_labels[-1].append(str((xmin +xmax)/2 * 1.0 /w))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((ymin +ymax)/2 * 1.0 /h))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((xmax-xmin) * 1.0 /w))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((ymax-ymin) * 1.0 /h))
            inline_labels[-1].append("\n")
        cnt+=1

    
    csvfile.close()
    csvfile_w = open("./1/train/"+filename[:-3]+"txt",mode='w')
    for r in inline_labels:
        csvfile_w.writelines(r)
    csvfile_w.close()
    cnt=1



cnt=1
for filename in os.listdir(r"train_20200620/GGO_PNG"):
    csvfile = open("train_20200620/GGO_Label/"+filename[:-4]+"_01.txt")
    reader = csv.reader(csvfile)
    print("train/GGO_PNG/"+filename)
    img=cv2.imread("train_20200620/GGO_PNG/"+filename)    
    #horizontal_img= cv2.flip(img,1)
    #vertical_img= cv2.flip(img,0)
    
    
    inline_labels = []

    #1111111111111111111111111111111111111111111111111111111111111111111111111
    inline_labels.append([])
   
    #inline_labels[-1].append("train/GGOPNG/"+filename[:-3]+".png ") #要改成絕對路徑
    
   
    w=img.shape[0]
    h=img.shape[1]
    img_resize=cv2.resize(img,(416,416))
    cv2.imwrite("./1/train/"+filename, img_resize)
    for line in reader:
        #if cnt!=1:
         #   inline_labels[-1].append(" ")
        if cnt%2!=0:
           
            inline_labels[-1].append(   str(    int(line[2]) -1   )     )
            inline_labels[-1].append(" ")
            xmin = int(line[0])
            ymin = int(line[1])
        else:
            xmax = int(line[0])
            ymax = int(line[1])
            inline_labels[-1].append(str((xmin +xmax)/2 * 1.0 /w))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((ymin +ymax)/2 * 1.0 /h))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((xmax-xmin) * 1.0 /w))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((ymax-ymin) * 1.0 /h))
            inline_labels[-1].append("\n")
        cnt+=1

    
    csvfile.close()
    csvfile_w = open("1/train/"+filename[:-3]+"txt",mode='w')
    for r in inline_labels:
        csvfile_w.writelines(r)
    csvfile_w.close()
    cnt=1

cnt=1
for filename in os.listdir(r"train_20200620/GGO_PNG"):
    csvfile = open("train_20200620/GGO_Label/"+filename[:-4]+"_01.txt")
    reader = csv.reader(csvfile)
    print("train/GGO_PNG/"+filename)
    img=cv2.imread("train_20200620/GGO_PNG/"+filename)    
    horizontal_img= cv2.flip(img,1)
    #vertical_img= cv2.flip(img,0)
    
    
    inline_labels = []

    #1111111111111111111111111111111111111111111111111111111111111111111111111
    inline_labels.append([])
   
    #inline_labels[-1].append("train/GGOPNG/"+filename[:-3]+".png ") #要改成絕對路徑
    
   
    w=img.shape[0]
    h=img.shape[1]
    img_resize=cv2.resize(horizontal_img,(416,416))
    cv2.imwrite("./1/train/"+filename[:-4]+'_horizontal.png', img_resize)
    for line in reader:
        #if cnt!=1:
         #   inline_labels[-1].append(" ")
        if cnt%2!=0:
           
            inline_labels[-1].append(   str(    int(line[2]) -1   )     )
            inline_labels[-1].append(" ")
            xmin = int(line[0])
            ymin = int(line[1])
        else:
            xmax = int(line[0])
            ymax = int(line[1])
            
            x1=w-xmax
            x2=w-xmin
            y1=ymin
            y2=ymax
            
            inline_labels[-1].append(str((x1 +x2)/2 * 1.0 /w))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((y1 +y2)/2 * 1.0 /h))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((x2-x1) * 1.0 /w))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((y2-y1) * 1.0 /h))
            inline_labels[-1].append("\n")
        cnt+=1
        
    

    
    csvfile.close()
    print(inline_labels)
    csvfile_w = open("1/train/"+filename[:-4]+"_horizontal.txt",mode='w')
    for r in inline_labels:
        csvfile_w.writelines(r)
    csvfile_w.close()
    cnt=1

cnt=1
for filename in os.listdir(r"train_20200620/GGO_PNG"):
    csvfile = open("train_20200620/GGO_Label/"+filename[:-4]+"_01.txt")
    reader = csv.reader(csvfile)
    print("train/GGO_PNG/"+filename)
    img=cv2.imread("train_20200620/GGO_PNG/"+filename)    
    #horizontal_img= cv2.flip(img,1)
    vertical_img= cv2.flip(img,0)
    
    
    inline_labels = []

    #1111111111111111111111111111111111111111111111111111111111111111111111111
    inline_labels.append([])
   
    #inline_labels[-1].append("train/GGOPNG/"+filename[:-3]+".png ") #要改成絕對路徑
    
   
    w=img.shape[0]
    h=img.shape[1]
    img_resize=cv2.resize(vertical_img,(416,416))
    cv2.imwrite("./1/train/"+filename[:-4]+'_vertical.png', img_resize)
    for line in reader:
        #if cnt!=1:
         #   inline_labels[-1].append(" ")
        if cnt%2!=0:
           
            inline_labels[-1].append(   str(    int(line[2]) -1   )     )
            inline_labels[-1].append(" ")
            xmin = int(line[0])
            ymin = int(line[1])
        else:
            xmax = int(line[0])
            ymax = int(line[1])
            
            x1=xmin
            x2=xmax
            y1=h-ymax
            y2=h-ymin
            
            inline_labels[-1].append(str((x1 +x2)/2 * 1.0 /w))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((y1 +y2)/2 * 1.0 /h))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((x2-x1) * 1.0 /w))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((y2-y1) * 1.0 /h))
            inline_labels[-1].append("\n")
        cnt+=1
        
    

    
    csvfile.close()
    print(inline_labels)
    csvfile_w = open("1/train/"+filename[:-4]+"_vertical.txt",mode='w')
    for r in inline_labels:
        csvfile_w.writelines(r)
    csvfile_w.close()
    cnt=1

cnt=1
for filename in os.listdir(r"train_20200620/LLL_PNG"):
    csvfile = open("train_20200620/LLL_Label/"+filename[:-4]+"_01.txt")
    reader = csv.reader(csvfile)
    print("train/LLL_PNG/"+filename)
    img=cv2.imread("train_20200620/LLL_PNG/"+filename)    
    #horizontal_img= cv2.flip(img,1)
    #vertical_img= cv2.flip(img,0)
    
    
    inline_labels = []

    #1111111111111111111111111111111111111111111111111111111111111111111111111
    inline_labels.append([])
   
    #inline_labels[-1].append("train/GGOPNG/"+filename[:-3]+".png ") #要改成絕對路徑
    
   
    w=img.shape[0]
    h=img.shape[1]
    img_resize=cv2.resize(img,(416,416))
    cv2.imwrite("./1/train/"+filename, img_resize)
    for line in reader:
        #if cnt!=1:
         #   inline_labels[-1].append(" ")
        if cnt%2!=0:
           
            inline_labels[-1].append(str(   int(line[2])-1    ))
            inline_labels[-1].append(" ")
            xmin = int(line[0])
            ymin = int(line[1])
        else:
            xmax = int(line[0])
            ymax = int(line[1])
            inline_labels[-1].append(str((xmin +xmax)/2 * 1.0 /w))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((ymin +ymax)/2 * 1.0 /h))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((xmax-xmin) * 1.0 /w))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((ymax-ymin) * 1.0 /h))
            inline_labels[-1].append("\n")
        cnt+=1

    
    csvfile.close()
    csvfile_w = open("1/train/"+filename[:-3]+"txt",mode='w')
    for r in inline_labels:
        csvfile_w.writelines(r)
    csvfile_w.close()
    cnt=1

cnt=1
for filename in os.listdir(r"train_20200620/LLL_PNG"):
    csvfile = open("train_20200620/LLL_Label/"+filename[:-4]+"_01.txt")
    reader = csv.reader(csvfile)
    print("train/LLL_PNG/"+filename)
    img=cv2.imread("train_20200620/LLL_PNG/"+filename)    
    horizontal_img= cv2.flip(img,1)
    #vertical_img= cv2.flip(img,0)
    
    
    inline_labels = []

    #1111111111111111111111111111111111111111111111111111111111111111111111111
    inline_labels.append([])
   
    #inline_labels[-1].append("train/GGOPNG/"+filename[:-3]+".png ") #要改成絕對路徑
    
   
    w=img.shape[0]
    h=img.shape[1]
    img_resize=cv2.resize(horizontal_img,(416,416))
    cv2.imwrite("./1/val/"+filename[:-4]+'_horizontal.png', img_resize)
    for line in reader:
        #if cnt!=1:
         #   inline_labels[-1].append(" ")
        if cnt%2!=0:
           
            inline_labels[-1].append(   str(    int(line[2]) -1   )     )
            inline_labels[-1].append(" ")
            xmin = int(line[0])
            ymin = int(line[1])
        else:
            xmax = int(line[0])
            ymax = int(line[1])
            
            x1=w-xmax
            x2=w-xmin
            y1=ymin
            y2=ymax
            
            inline_labels[-1].append(str((x1 +x2)/2 * 1.0 /w))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((y1 +y2)/2 * 1.0 /h))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((x2-x1) * 1.0 /w))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((y2-y1) * 1.0 /h))
            inline_labels[-1].append("\n")
        cnt+=1
        
    

    
    csvfile.close()
    print(inline_labels)
    csvfile_w = open("1/val/"+filename[:-4]+"_horizontal.txt",mode='w')
    for r in inline_labels:
        csvfile_w.writelines(r)
    csvfile_w.close()
    cnt=1

cnt=1
for filename in os.listdir(r"train_20200620/Pneumonia_PNG"):
    csvfile = open("train_20200620/Pneumonia_Label/"+filename[:-4]+"_01.txt")
    reader = csv.reader(csvfile)
    print("train/Pneumonia_PNG/"+filename)
    img=cv2.imread("train_20200620/Pneumonia_PNG/"+filename)    
    #horizontal_img= cv2.flip(img,1)
    #vertical_img= cv2.flip(img,0)
    
    
    inline_labels = []

    #1111111111111111111111111111111111111111111111111111111111111111111111111
    inline_labels.append([])
   
    #inline_labels[-1].append("train/GGOPNG/"+filename[:-3]+".png ") #要改成絕對路徑
    
   
    w=img.shape[0]
    h=img.shape[1]
    img_resize=cv2.resize(img,(416,416))
    cv2.imwrite("./1/train/"+filename, img_resize)
    for line in reader:
        #if cnt!=1:
         #   inline_labels[-1].append(" ")
        if cnt%2!=0:
           
            inline_labels[-1].append(str(   int(line[2])-1    ))
            inline_labels[-1].append(" ")
            xmin = int(line[0])
            ymin = int(line[1])
        else:
            xmax = int(line[0])
            ymax = int(line[1])
            inline_labels[-1].append(str((xmin +xmax)/2 * 1.0 /w))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((ymin +ymax)/2 * 1.0 /h))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((xmax-xmin) * 1.0 /w))
            inline_labels[-1].append(" ")
            inline_labels[-1].append(str((ymax-ymin) * 1.0 /h))
            inline_labels[-1].append("\n")
        cnt+=1

    
    csvfile.close()
    csvfile_w = open("1/train/"+filename[:-3]+"txt",mode='w')
    for r in inline_labels:
        csvfile_w.writelines(r)
    csvfile_w.close()
    cnt=1

# +
w_file=open("1/train.list",'w')

for filename in os.listdir(r"train_20200620/GGO_PNG"):
    w_file.writelines("/home/kuo4567654/1/train/"+filename+'\n')
    w_file.writelines("/home/kuo4567654/1/train/"+filename[:-4]+'_horizontal.png\n')
    w_file.writelines("/home/kuo4567654/1/train/"+filename[:-4]+'_vertical.png\n')
    print(filename)
    
for filename in os.listdir(r"train_20200620/LLL_PNG"):
    w_file.writelines("/home/kuo4567654/1/train/"+filename+'\n')
    print(filename)

    
for filename in os.listdir(r"train_20200620/Pneumonia_PNG"):
    w_file.writelines("/home/kuo4567654/1/train/"+filename+'\n')
    print(filename)
# +
w_file=open("1/val.list",'a')

for filename in os.listdir(r"train_20200620/LLL_PNG"):
    w_file.writelines("/home/kuo4567654/1/val/"+filename[:-4]+'_horizontal.png\n')
    print(filename)

   
# -



