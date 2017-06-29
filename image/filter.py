from PIL import Image
import pylab as plt
import numpy as np
import cv2
import imtools
import scipy.misc 

#im1 = np.array(Image.open('/home/jcshin/Pictures/trumper.jpg'))
im1 = np.array(Image.open('/home/jcshin/Pictures/trumper.jpg').convert('L'))
im4 = np.array(Image.open('/home/jcshin/Pictures/car.jpg').convert('L'))
im5 = np.array(Image.open('/home/jcshin/Pictures/castle.jpg').convert('L'))

# Simple Image Processing
#im2 = 255 - im1 # inversion
#im2 = np.uint8((100.0/255)*im1 + 100)
#im2 = 255.0*(im1/255.0)**2

# Histogram Equalization
#im2, cdf = imtools.histeq(im1)

# Image Averaging
im2 = imtools.compute_average(['/home/jcshin/Pictures/trumper.jpg','/home/jcshin/Pictures/car.jpg'])

# scipy.misc image resize
#im2 = scipy.misc.imresize(im4,im1.shape,interp='bilinear')

print im1.dtype, im1.shape, im1.min(), im1.max(), im1.mean()
print im2.dtype, im2.shape, im2.min(), im2.max(), im2.mean()

#cv2.imshow('im2',im2)

plt.figure()
plt.gray()
plt.subplot(211); plt.imshow(im1); plt.axis('equal'); plt.axis('off')
plt.subplot(212); plt.imshow(im2); plt.axis('equal'); plt.axis('off')
plt.show()




