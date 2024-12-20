import os
import time
import subprocess
import cv2
from matplotlib import pyplot as plt

process1 = subprocess.Popen(f"ffmpeg -f v4l2 -i /dev/video0 -frames:v 1 image22.png", shell=True)
print("Image 1 capture started.")


process2 = subprocess.Popen(f"ffmpeg -f v4l2 -i /dev/video2 -frames:v 1 image33.png", shell=True)
print("Image 2 capture started.")


process1.wait()
process2.wait()

print("Both images captured successfully.")



image1 = cv2.imread('/home/BVB/image22.png')
image2 = cv2.imread('/home/BVB/image33.png')


image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
image2_rgb = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)


fig, ax = plt.subplots(1, 2, figsize=(14, 10))
ax[0].imshow(image1_rgb)
ax[0].set_title("Part 1")
ax[0].axis("off")
ax[1].imshow(image2_rgb)
ax[1].set_title("Part 2")
ax[1].axis("off")
plt.show()

stitcher = cv2.Stitcher_create()


status, stitched_image = stitcher.stitch((image1, image2))

if status == cv2.Stitcher_OK:
    
    stitched_image_rgb = cv2.cvtColor(stitched_image, cv2.COLOR_BGR2RGB)
    
    # Display the stitched image
    plt.figure(figsize=(14, 10))
    plt.imshow(stitched_image_rgb)
    plt.title('Stitched Image')
    plt.axis("off")
    plt.show()
elif status == cv2.Stitcher_ERR_NEED_MORE_IMGS:
    print('Not enough images for stitching.')
elif status == cv2.Stitcher_ERR_HOMOGRAPHY_EST_FAIL:
    print('Homography estimation failed.')
else:
    print('Image stitching failed!')
