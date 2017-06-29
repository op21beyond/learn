from PIL import Image
import numpy as np
import scipy.misc 

def imresize(im,sz): 
   """ Resize an image array using PIL. """ 
   pil_im = Image.fromarray(uint8(im)) 
   return np.array(pil_im.resize(sz))


def histeq(im, nbr_bins=256):
   """ histogram equalization of a grayscale image. """
   imhist,bins = np.histogram(im.flatten(),nbr_bins,normed=True)
   cdf = imhist.cumsum()
   cdf = 255*cdf / cdf[-1]
   im2 = np.interp(im.flatten(), bins[:-1],cdf)
   return im2.reshape(im.shape), cdf

def compute_average(imlist):
   """ compute the average of a list of images """
   averageim = np.array(Image.open(imlist[0]),'f')

   for imname in imlist[1:]:
      try:
         averageim += scipy.misc.imresize(np.array(Image.open(imname),'f'),averageim.shape,interp='bilinear')
      except:
         print (imname + ' ... Skipped')
   averageim /= len(imlist)
   return np.array(averageim, 'uint8')
