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
# TODO infinite zooming effect
## implement different feature extrators, e.g. SIFT, SURF, and compare the results 

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
### image compare 

all method draw 2000 feature keypoint

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
