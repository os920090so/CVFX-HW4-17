# CVFX-HW4-17
## Take a sequence of moving-forward images in NTHU campus.
![](https://i.imgur.com/lNqXKBW.png)  
## Show feature extraction and matching results between two images 
feature extraction using ORB method (number of feature = 500)  
![](https://i.imgur.com/Wwx4aGN.png)  
matching in RGB image (matching number = 75)  
![](https://i.imgur.com/jQ3wZDW.jpg)  
## Perform image alignment and generate infinite zooming effect 
let the image on the right side aligned with the image on the left side

| left | right |
| -------- | -------- |
| ![](https://i.imgur.com/xUsY47g.jpg)| ![](https://i.imgur.com/ToQjcr9.jpg) |
## infinite zooming effect
[![ERROR](https://img.youtube.com/vi/88LUi5Nmv4Q/0.jpg)](https://www.youtube.com/watch?v=88LUi5Nmv4Q)  
## implement different feature extrators, e.g. SIFT, SURF, and compare the results 
we implement following methods. We will first summary the feature extrators and then show image results of different methods. 
### SIFT
SIFT is propsed by D.Lowe, University of British Columbia in his paper, Distinctive Image Features from Scale-Invariant Keypoints, which extract keypoints and compute its descriptors. There are mainly four steps in SIFT.  
1.Scale-space Extrema Detection -- use difference of Gaussians to approximate LoG and search local extrema over scale and space.  
2.Keypoint Localization -- In order to refine the potential key points, They used Taylor series expansion of scale space and a concept similar to Harris corner detector to get more accurate location of extrema.  
3.Orientation Assignment -- They assign the orientation to achieve invariance to image rotation and creates keypoints with same location and scale, but different directions.  
4.Keypoint Descriptor -- Take 16*16 neighbourhood around the keypoint and divided it into 16 sub-blocks of 4x4 size.For each sub-block, 8 bin orientation histogram is created. So a total of 128 bin values are available.
### SURF
SURF stands for Speeded Up Robust Features. SURF goes a little further and approximates LoG with Box Filter which can be easily calculated with the help of integral images. And it can be done in parallel for different scales.
### USURF
SURF without calculating orientation.
### ORB
ORB came from "OpenCV Labs". Compare with SIFT and SURF, the main advantage for ORB is that you are not supposed to pay for its use. ORB is basically a fusion of FAST keypoint detector and BRIEF descriptor with many modifications to enhance the performance. 
## image compare 
To easily compare, we modify the threadhold of SURF/USURF and feature number of SIFT/ORB so that all method detect 2000 feature keypoint.

| orgin | SIFT |
| -------- | -------- |
| ![](https://i.imgur.com/aoiBvUj.jpg) | ![](https://i.imgur.com/zd1HQaF.jpg) |

| SURF | USURF |
| -------- | -------- |
| ![](https://i.imgur.com/Vq2A58A.jpg)| ![](https://i.imgur.com/N22k0t5.jpg) |
 
| ORB | orgin |
| -------- | -------- |
| ![](https://i.imgur.com/0uajTNi.jpg)| ![](https://i.imgur.com/sLmeaec.jpg) |

| SIFT | SURF |
| -------- | -------- |
| ![](https://i.imgur.com/20R404k.jpg)| ![](https://i.imgur.com/P4EjEl7.jpg)|

| USURF | ORB |
| -------- | -------- |
| ![](https://i.imgur.com/O4TmWeC.jpg)| ![](https://i.imgur.com/z9n5E4D.jpg)|  
  
**SIFT** : Most feature's scale are small. Since the OpenCV document said the features are ranked by the local contrast. We guess that the smaller the scale is, the higher the local contrast of feature is.  
**SURF/USURF** : As you can see in the car image, SURF not only detect the car but also detect some objects in the back ground. The average scale of keypoints is between SIFT and ORB. The only difference between SURF and USURF is the latter's orientations are shown in same direction while the former are not.  
**ORB** : The scale of features are much larger than others. Specially focus on some region result in a lot of overlapping.  
### experiment & analysis
We also conduct the experiment of execution time based on python timeit (calculate average from 100 loops).  

| descroption | SIFT | SURF | USURF | ORB | 
| -------- | -------- | -------- | -------- | -------- | 
| execution time (sec)     |  0.157   | 0.112     | 0.060     | 0.037     |
| for business usage | need pay | need pay | need pay | free |
| most feature scale | small | medium | medium | big | 
| feature distribution     | equally | equally | equally | centrally     | 
