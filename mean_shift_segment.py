# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 13:54:50 2020

@author: ADMIN-PC
"""
import cv2
import numpy as np
from skimage import color
from numpy.linalg import norm
import matplotlib.pyplot as plt
import random

def mean_shift_segment(img,thresh,S):
    row=img.shape[0]
    col=img.shape[1]
    J= row * col
    Size = (row,col,3)
    
    #intialising images for mean shift segment and avg_saliency img for each segment 
    R = np.zeros(Size, dtype= np.uint8)
    at=np.zeros((row,col), dtype= np.uint8)
    
    D=np.zeros((J,5))
    counter=0  
    it=1   
    threshold=thresh
    current_mean_random = True
    current_mean_arr = np.zeros((1,5))
    below_threshold_arr=[]

    # converted the image img[rows][col] into a feature space D. The dimensions of D are [rows*col][5]

    for i in range(0,row):
        for j in range(0,col):      
            arr= img[i][j]
            for k in range(0,5):
                if(k>=0) & (k <=2):
                    D[counter][k]=arr[k]
                else:
                    if(k==3):
                        D[counter][k]=i
                    else:
                        D[counter][k]=j
            counter+=1

#mean shift code
#choosing a random row in D as mean
    while(len(D) > 0):    
        if(current_mean_random):
            current_mean= random.randint(0,len(D)-1)
            for i in range(0,5):
                current_mean_arr[0][i] = D[current_mean][i]
        below_threshold_arr=[]
        
#finding euclidean distance of all other rows from the current mean row.

        for i in range(0,len(D)):
            ecl_dist = 0
            for j in range(0,5):
                 ecl_dist += ((current_mean_arr[0][j] - D[i][j])**2)
            ecl_dist = ecl_dist**0.5
#if distance is below the threshold then index of that row is taken in the below_threshold_arr.      
            if(ecl_dist < threshold):
                 below_threshold_arr.append(i)
        mean_R=0
        mean_G=0
        mean_B=0
        mean_i=0
        mean_j=0
        
#for all the index of elements in below_threshold_arr finding mean of each color channel and coordinates   
        for i in range(0, len(below_threshold_arr)):
            mean_R += D[below_threshold_arr[i]][0]
            mean_G += D[below_threshold_arr[i]][1]
            mean_B += D[below_threshold_arr[i]][2]
            mean_i += D[below_threshold_arr[i]][3]
            mean_j += D[below_threshold_arr[i]][4]   
    
        mean_R = mean_R / len(below_threshold_arr)
        mean_G = mean_G / len(below_threshold_arr)
        mean_B = mean_B / len(below_threshold_arr)
        mean_i = mean_i / len(below_threshold_arr)
        mean_j = mean_j / len(below_threshold_arr)
        
#finding the distance from the means to the random mean row.

        mean_e_distance = ((mean_R - current_mean_arr[0][0])**2 + (mean_G - current_mean_arr[0][1])**2 + (mean_B - current_mean_arr[0][2])**2 + (mean_i - current_mean_arr[0][3])**2 + (mean_j - current_mean_arr[0][4])**2)
        mean_e_distance = mean_e_distance**0.5
#if the distance is below a threshold then that random mean is continued else the means calculatded as taken as current mean    
       
        if(mean_e_distance < it):
            new_arr = np.zeros((1,3))
            new_arr[0][0] = mean_R
            new_arr[0][1] = mean_G
            new_arr[0][2] = mean_B
            mean_seg=0
            
            # assigning the mean values to all the elements in below_threshold_arr.
            #for all indexes in below_threshold_arr,calucating avg saliency and assigning tht value to all indices.
            
            for i in range(0, len(below_threshold_arr)):    
                R[int(D[below_threshold_arr[i]][3])][int(D[below_threshold_arr[i]][4])] = new_arr
                D[below_threshold_arr[i]][0] = -1
                mean_seg+=S[int(D[below_threshold_arr[i]][3]),int(D[below_threshold_arr[i]][4])]
            mean_seg=mean_seg/len(below_threshold_arr)
            for i in range(0, len(below_threshold_arr)):
                at[int(D[below_threshold_arr[i]][3])][int(D[below_threshold_arr[i]][4])]=mean_seg
            current_mean_random = True
            new_D=np.zeros((len(D),5))
            counter_i = 0
            
            #finding a new_D array with the left over indices(other than below_threshold_arr)
            
            for i in range(0, len(D)):
                if(D[i][0] != -1):
                    new_D[counter_i][0] = D[i][0]
                    new_D[counter_i][1] = D[i][1]
                    new_D[counter_i][2] = D[i][2]
                    new_D[counter_i][3] = D[i][3]
                    new_D[counter_i][4] = D[i][4]
                    counter_i += 1
            
        
            D=np.zeros((counter_i,5))
            counter_i -= 1
            for i in range(0, counter_i):
                D[i][0] = new_D[i][0]
                D[i][1] = new_D[i][1]
                D[i][2] = new_D[i][2]
                D[i][3] = new_D[i][3]
                D[i][4] = new_D[i][4]
        else:
            current_mean_random = False
         
            current_mean_arr[0][0] = mean_R
            current_mean_arr[0][1] = mean_G
            current_mean_arr[0][2] = mean_B
            current_mean_arr[0][3] = mean_i
            current_mean_arr[0][4] = mean_j
    return R,at