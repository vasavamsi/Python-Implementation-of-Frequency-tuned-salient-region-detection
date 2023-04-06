# Python-Implementation-of-Frequency-tuned-salient-region-detection
This is an adaption of the paper https://ieeexplore.ieee.org/abstract/document/5206596/ as a part of Course project in Computer Vision course

Introduction to the Paper:
Saliency of the pixel determines it to outstand from the point of visual perception with respect to the other neighbouring pixels. This paper introduces the simply implementable algorithm for detecting the Saliency map and Segmenting the Salient feature using this S-map. This paper would further be helpful for obtaining adaptive data delivery, Adaptive image compression (to retain the Salient attributes), Object segmentation and recognition.
The paper introduces uniformly distributed salient map extraction technique from involving colour and luminescence of the image. This would lead to well-defined boundaries, full resolution and computational efficiency.
Frequency-tuned Saliency Detection:
The approach is to pertain several bands of frequencies to obtain the saliency map, and to obtain the same DoG filter is used. The flow of Algorithm is explained here with an example.

![image](https://user-images.githubusercontent.com/58003228/230462806-49636390-8a18-421a-88a9-62a3b6c2b401.png)

Fig: Original image

> Obtain the mean value pixel in the Lab format.
> Obtain the Gaussian filtered image from the Lab format. The kernel used is (1/16)*[1,4,6,4,1].
> Saliency map is obtained from the L2 norm between mean value pixel and Gaussian filtered image.

![image](https://user-images.githubusercontent.com/58003228/230463223-9037633e-6831-4fff-949f-85f85f3cc949.png)

Fig: Saliency map

> For the implementation of  Segmentation by Fixed threshold, we implemented  binary masking on saliency map with fixed threshold (can be changed as per user evaluation, same is mentioned in the test_script.py)

![image](https://user-images.githubusercontent.com/58003228/230463380-f01bbe75-05b4-4f3c-8355-442e617c743c.png)

Fig: Fixed threshold segmented image

> For the implementation of Segmentation by Adaptive threshold, we obtained mean shift segmentation of the RGB image.

![image](https://user-images.githubusercontent.com/58003228/230463487-19af455d-c2b7-41ef-8cc4-867caf347102.png)

Fig: Mean segmented image

> Calculate the avg. saliency value of the segments.

![image](https://user-images.githubusercontent.com/58003228/230463581-47395f1a-c023-463b-ad87-4fdfa908cce3.png)

Fig: Mean segmented saliency map

> Compare avg. saliency value with the mean saliency value obtained from the map times the k factor (k factor is explained later). The k factor used claimed in the paper is 2. If this avg. saliency value is greater, retain the segment or else discard.

![image](https://user-images.githubusercontent.com/58003228/230463649-901cc389-bf94-431b-92b8-8f16fa30e5c1.png)

Fig: Adaptive segmented image
