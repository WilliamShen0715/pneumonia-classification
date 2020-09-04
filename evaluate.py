# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 15:52:34 2020

@author: William


here for evaluation:
    
1.put test pictures in :
    /1/val/
2.show the index of picture in :
    /1/val/val.list
3.cd /darknet
4.run the commands showed in README on command line or run the following script:
"""
import os
#here for model evaluation
os.system("./darknet detector recall cfg/cat_and_dog.data cfg/cat_and_dog_yolov3.cfg backup/cat_and_dog_yolov3_final.weights")
#%%
#here for testing picture
#change the picture's name to test data's
os.system("./darknet detector test cfg/cat_and_dog.data cfg/cat_and_dog_yolov3.cfgbackup/cat_and_dog_yolov3_final.weights /home/kuo4567654/1/val/LLL009801.png")