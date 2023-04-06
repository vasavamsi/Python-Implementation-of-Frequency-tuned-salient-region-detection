# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 14:20:57 2020

@author: ADMIN-PC
"""
import numpy as np

def final_segmentation(S, img, at, k = 2):
    ta=k*(np.mean(S)) # Calculating the threshold to compare
    
    ## Getting the binary mask
    ab=np.zeros(at.shape,dtype=np.uint8)
    for i in range(at.shape[0]):
        for j in range(at.shape[1]):
            if at[i][j]>=ta:
                ab[i,j]=0  # Here the values can be interchanged to get the user interested region 
            else:            #judging from salient map
                ab[i,j]=255    
    
    ## Getting the final segmented image with adaptive thresholding
    F=np.zeros(img.shape,dtype=np.uint8)
    for i in range(at.shape[0]):
        for j in range(at.shape[1]):
            if ab[i][j]==255:
                F[i,j,:]=img[i,j,:]
    return ab, F