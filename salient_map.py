# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 18:54:24 2020

@author: ADMIN-PC
"""
import cv2
import numpy as np
from skimage import color
from numpy.linalg import norm

def salient_map(img):
    """
    Arguments: 
    img = RGB image for obtaining the salient map
    
    Returns:
    S = Salient map for the input RGB image in uint8 format
    """
    # Getting mean value pixel in Lab format
    img_R = np.array(img[:,:,0])
    img_G = np.array(img[:,:,1])
    img_B = np.array(img[:,:,2])
    
    mean_R = int(np.mean(img_R))
    mean_G = int(np.mean(img_G))
    mean_B = int(np.mean(img_B))
    
    mean_img = np.zeros([img.shape[0], img.shape[1], 3])
    mean_img[:,:,0] = np.ones((img.shape[0], img.shape[1])) * mean_R 
    mean_img[:,:,1] = np.ones((img.shape[0], img.shape[1])) * mean_G
    mean_img[:,:,2] = np.ones((img.shape[0], img.shape[1])) * mean_B
    
    mean_lab = color.rgb2lab(mean_img)
    
    # Getting Gaussian blurred image in Lab format
    K = np.array([1,4,6,4,1], dtype = float) * 1/16
    K = np.reshape(K, (1,5))
    kernel = np.dot(K.T,K)
    
    Gauss_img = cv2.filter2D(img, -1, kernel)
    
    Gauss_lab = color.rgb2lab(Gauss_img)
    
    # Getting salient map
    S_map = norm(mean_lab - Gauss_lab, axis=2)
    S = S_map.astype('uint8')
    
    return S