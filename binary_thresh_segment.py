# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 19:03:27 2020

@author: ADMIN-PC
"""
import cv2
import numpy as np

def binary_tresh_segment(S, img, tresh):
    """
    Arguments:
    S = Salient map
    img = input RGB image
    tresh = fixed threshold value
    
    Returns:
    tresh_bin = tresholded binary image
    seg_img = segmented image
    """
    # Binary thresholding the saliency map
    ret, tresh_bin = cv2.threshold(S, tresh, 255, cv2.THRESH_BINARY)
    
    # Getting the segmentation after binary thresholding
    seg_img = np.zeros(img.shape)
    for i  in range(tresh_bin.shape[0]):
        for j in range(tresh_bin.shape[1]):
            if tresh_bin[i,j] == 0:
                seg_img[i,j,:] = img[i,j,:]
                
    return tresh_bin, seg_img