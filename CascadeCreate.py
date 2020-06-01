#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:37:38 2020

@author: dogukangundogan
"""
import os
import cv2
import numpy as np
import urllib.request
def store_image():
    neg_url=urllib.request.urlopen("http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00007846").read().decode()
    if not os.path.exists("neg"):
         os.makedirs("neg")
    num=1
    
    for i in neg_url.split("\n"):
        try:
            urllib.request.urlretrieve(i,"neg/"+str(num)+".jpg")
            img=cv2.imread("neg/"+str(num)+".jpg",cv2.IMREAD_GRAYSCALE)
            resize=cv2.resize(img,(100,100))
            cv2.imwrite("neg/"+str(num)+".jpg", resize)
            num+=1
        except Exception as e:
            print(str(e))
def clean_photos():
    if not os.path.exists("uglies"):
         os.makedirs("uglies")
    for file_types in ['neg']:
        for img in os.listdir(file_types):
            for ugly in os.listdir("uglies"):
                try:
                    current_path=str(file_types)+"/"+str(img)
                    ugly=cv2.imread("uglies/"+str(ugly))
                    question=cv2.imread(current_path)
                    if ugly.shape==question.shape and not(np.bitwise_xor(ugly,question).any()):
                        os.remove(current_path )
                except Exception as e:
                    print(str(e))
                    
def create_post_n_neg():
    for file_types in ['neg']:
        for img in os.listdir(file_types):
            if file_types=='neg':
                line=file_types+"/"+str(img)+"\n"
                with  open("bg.txt","a")  as f:
                    f.write(line)
            elif file_types=='pos':
                line=file_types+"/"+str(img)+"1 0 0 50 50\n"
                with  open("info.dat","a")  as f:
                    f.write(line)
                 
#store_image()
#clean_photos()
#create_post_n_neg()
 
