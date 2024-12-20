# ImageStitchingUsingRaspberrypi
Image stitching with Raspberry Pi 4 involves capturing overlapping images using cameras like the Pi Camera Module. These images are aligned based on features using algorithms such as SIFT or ORB. Software like OpenCV processes the images to create a seamless panorama. The Pi 4's robust CPU and GPU make it suitable for real-time stitching in lightweight setups.
# Functional block diagram

<img src="https://github.com/user-attachments/assets/db5e9ff8-2b53-45c7-80e8-0c066e2e252a" width="500">

# METHODOLOGY
Setup Hardware:
Connect the Pi Camera Module(s) to the Raspberry Pi 4.
Mount the camera for stable image capture, ensuring overlapping fields of view.

Capture Images:Use Python with picamera or OpenCV to capture sequential images.
Ensure about 30-50% overlap between consecutive images for better stitching.

Preprocessing:Convert images to grayscale for faster processing.
Apply noise reduction (e.g., Gaussian blur) to improve feature detection.

Feature Detection:Use OpenCV methods like SIFT, SURF, or ORB to identify key points and descriptors in the overlapping areas.

Feature Matching:Match features between consecutive images using techniques like FLANN or BFMatcher to find corresponding points.

Homography Estimation:Compute the transformation matrix (homography) to align one image onto the other.
Use RANSAC to eliminate outliers and improve accuracy.

Image Warping:Warp the images based on the computed homography to align them spatially.

Blending:Seamlessly blend overlapping regions using feathering, multi-band blending, or alpha blending to reduce visible seams.

Output Panorama:Merge aligned images into a single panoramic output using OpenCV’s stitching functions.

Optimization:Optimize code to run efficiently on the Pi 4 by leveraging its GPU with OpenCL or using lightweight libraries.

Display/Save:Display the panorama on a connected screen or save it using supported formats (e.g., PNG or JPEG).

# Results

<div style="text-align: center;">
    <img src="https://github.com/user-attachments/assets/7e1785d6-b7be-4da0-b90b-9e4458dabda8" width="400" style="margin-right: 20px;">
    <p>INPUT IMAGE1</p>
</div>

<div style="text-align: center;">
    <img src="https://github.com/user-attachments/assets/c2d14c68-1934-430c-95ec-cf4a5b58ca5d" width="400" style="margin-right: 20px;">
    <p>INPUT IMAGE2</p>
</div>

<div style="text-align: center;">
    <img src="https://github.com/user-attachments/assets/2aa132ef-c94d-409e-b736-f67af81576b7" width="400">
    <p>STITCHED IMAGE</p>
</div>
<img src="https://github.com/user-attachments/assets/752a8172-8a71-47cc-bd41-26786032a952" width="500">
<img src="https://github.com/user-attachments/assets/07ac4c08-2774-485a-98aa-2064d389de2a" width="500">

