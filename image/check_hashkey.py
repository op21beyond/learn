import numpy as np
import cv2
import matplotlib.pyplot as plt
import scipy.misc
import scipy.ndimage.filters as filters
from hashTable import hashTable


Qangle = 24
Qstrenth = 3
Qcoherence = 3

if True:
   #img = scipy.misc.imread("../train/a.jpg",mode='L')
   img = scipy.misc.imread("/home/jongchul/workspace/yaraisr/bufferfly.jpg",mode='L')

if False:
   img = np.zeros((200,200))
   cv2.circle(img,(100,100),50,color=255,thickness=4)
   cv2.rectangle(img,(10,10),(190,190),color=255,thickness=4)

if False:
   img = np.zeros((200,200))
   img[100,100]=255.0
   cv2.circle(img,(100,100),20,color=255,thickness=4)
   #img = filters.gaussian_filter(img,sigma=100.0)
   img = filters.gaussian_filter(img,sigma=50.0)
   #img = filters.gaussian_filter(img,sigma=10.0)


out = np.zeros((img.shape[0],img.shape[1],3))
print (out.shape)

nx=0
ny=0
for x in range(5,img.shape[0]-6):
    for y in range(5,img.shape[1]-6):
        patch = img[x-4:x+5,y-4:y+5]
        angle,strength,coherence = hashTable(patch,Qangle,Qstrenth,Qcoherence)
        out[nx,ny] = (angle,strength,coherence)
        ny+=1
    nx+=1
    ny=0
    
plt.figure()
plt.subplot(221); plt.axis('off'); plt.title('input'); plt.imshow(img,cmap='gray')
plt.subplot(222); plt.axis('off'); plt.title('angle'); plt.imshow(out[:,:,0],cmap='gray')
plt.subplot(223); plt.axis('off'); plt.title('strength'); plt.imshow(out[:,:,1],cmap='gray')
plt.subplot(224); plt.axis('off'); plt.title('coherence'); plt.imshow(out[:,:,2],cmap='gray')
plt.show()

          
     
