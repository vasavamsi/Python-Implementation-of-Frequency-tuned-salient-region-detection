import cv2
from salient_map import salient_map
from binary_thresh_segment import binary_tresh_segment
from mean_shift_segment import mean_shift_segment
from final_segmentation import final_segmentation

input_path = './dataset/'
results_path = './results/'

image_name = '8.jpg' # change the name as per required
img = cv2.imread(input_path + image_name) # Change the no. to run the code on other image

## Getting saliency map from RGB image and saving it
S = salient_map(img)
cv2.imwrite(results_path + '1_salient_map.jpg', S)
print('Salient map is saved to the results folder')
print('......................................................')

## Getting the segmentation with fixed thresholding and saving to the root directory
tresh_bin, seg_img = binary_tresh_segment(S, img, tresh = 60) #threshold value can be changes as per user requirement
cv2.imwrite(results_path +'2_binary_thrsh_image.jpg', tresh_bin.astype('uint8'))
cv2.imwrite(results_path +'3_segmented_image.jpg', seg_img)
print('fixed threshold binary image and segmented image are saved to the results folder')
print('......................................................')

## Getting mean shift segmentation from the original image and saving to the root directory
R,at=mean_shift_segment(img,60,S) #This is the threshold for maintaining the similar kind of colour segments 
cv2.imwrite(results_path +'4_mean_segmeted_image.jpg',R)   #and can be varied as per user requirement
cv2.imwrite(results_path +'5_segmented_avg_saliency_map.jpg',at)
print('mean segmented image and average segmented saliency map are saved to the results folder')
print('......................................................')

## Getting the segmentation with adaptive thresholding
bin_img, fin_img = final_segmentation(S, img, at, k = 1.1) #The k factor can be changed according to the user
cv2.imwrite(results_path +'6_binary_adaptive_thresh_image.jpg',bin_img)
cv2.imwrite(results_path +'7_adaptive_segmented_image.jpg',fin_img)
print('adaptive thresholded binary image and segmented image are saved to the results folder')
print('......................................................')
