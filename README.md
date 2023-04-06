# Python-Implementation-of-Frequency-tuned-salient-region-detection
This is an adaption of the paper https://ieeexplore.ieee.org/abstract/document/5206596/ as a part of Course project in Computer Vision course

Introduction to the Paper:
Saliency of the pixel determines it to outstand from the point of visual perception with respect to the other neighbouring pixels. This paper introduces the simply implementable algorithm for detecting the Saliency map and Segmenting the Salient feature using this S-map. This paper would further be helpful for obtaining adaptive data delivery, Adaptive image compression (to retain the Salient attributes), Object segmentation and recognition.
The paper introduces uniformly distributed salient map extraction technique from involving colour and luminescence of the image. This would lead to well-defined boundaries, full resolution and computational efficiency.
Frequency-tuned Saliency Detection:
The approach is to pertain several bands of frequencies to obtain the saliency map, and to obtain the same DoG filter is used. The flow of Algorithm is explained here with an example.
 
Fig: Original image

	Obtain the mean value pixel in the Lab format.
	Obtain the Gaussian filtered image from the Lab format. The kernel used is (1/16)*[1,4,6,4,1].
	Saliency map is obtained from the L2 norm between mean value pixel and Gaussian filtered image.
 
Fig: Saliency map
	
	For the implementation of  Segmentation by Fixed threshold, we implemented  binary masking on saliency map with fixed threshold (can be changed as per user evaluation, same is mentioned in the test_script.py)
 
Fig: Fixed threshold segmented image

	For the implementation of Segmentation by Adaptive threshold, we obtained mean shift segmentation of the RGB image.
 
Fig: Mean segmented image

	Calculate the avg. saliency value of the segments.
 
Fig: Mean segmented saliency map

	Compare avg. saliency value with the mean saliency value obtained from the map times the k factor (k factor is explained later). The k factor used claimed in the paper is 2. If this avg. saliency value is greater, retain the segment or else discard.
 
Fig: Adaptive segmented image
Results on other images:

                              
            Original                                    Saliency map
               
 Mean segmented image          Mean segmented saliency map                     

                                            
                  Original                                               Saliency map                                                          Final segmented image
             
    Mean segmented image                         Mean segmented saliency map
                                  
                 Original Image	                                                                          Final Segmented image
                                             
                 Original Image	                                                                          Final Segmented image

Observations:
	The paper works much better if the salient feature to be segmented in the image is much darker than the background. As shown below, the saliency is much more highlighted in the parts of dark pixels.

                                     
Fig: (From left to right) the original image in RGB channel, the saliency map of the image, final segmented image with adaptive threshold

	If the image has uniform intensity it would become difficult to obtain the perfect segmentation.
                  
             Original image                                                     Final segmented image

	If the user’s region of interest is coming from the dark part of the salient map, the binary parts can be switched (same is mentioned in the code). As saliency is depended on the colour space and intensity.
                         
              Original Image	                         Before switching the binary part   	       After switching the binary part

	Paper claims k factor to be 2, but we observed that it is adaptive to image and can’t be fixed. Here the results provided after tuning the k factor (approx. 1.1) to get the good results.


 


























References:
1.	Paper reference: 
R. Achanta, S. Hemami, F. Estrada and S. Susstrunk, "Frequency-tuned salient region detection," 2009 IEEE Conference on Computer Vision and Pattern Recognition, Miami, FL, 2009, pp. 1597-1604, doi: 10.1109/CVPR.2009.5206596.
2.	https://docs.opencv.org/master/d7/d00/tutorial_meanshift.html
3.	http://luthuli.cs.uiuc.edu/~daf/courses/CS-498-DAF-PS/Segmentation.pdf
4.	http://home.ku.edu.tr/mehyilmaz/public_html/mean-shift/00400568.pdf
5.	https://www.mathworks.com/matlabcentral/fileexchange/10161-mean-shift-clustering
