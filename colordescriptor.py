# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 19:23:06 2016

@author: yang
"""
#%%
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')


import cv2
import numpy as np
from skimage.feature import hog
from skimage import data, color, exposure 
import matplotlib.pyplot as plt
#print cv2.__version__
#print "in descriptor.py"


np.set_printoptions(threshold='nan')
class ColorDescriptor:
	def __init__(self, bins):
		# store the number of bins for the 3D histogram
		self.bins = bins
  
 
	def describe(self, image):
		# convert the image to the HSV color space and initialize
		# the features used to quantify the image
		features=[]
		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#		image = color.rgb2gray(data.astronaut())
		fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualise=True)
#		cv2.imwrite('file.jpg',hog_image) 
#		cv2.imwrite('file1.jpg',image)
#		fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)
#		ax1.axis('off')
#		ax1.imshow(image, cmap=plt.cm.gray)
#		ax1.set_title('Input image')
#		ax1.set_adjustable('box-forced')       


#		sift = cv2.xfeatures2d.SIFT_create()
#		kp, des = sift.detectAndCompute(image,None)
		#print des,"feature"
#		print fd,"feature"
#		print fd.shape,"len"
		features.append(fd)


#		# grab the dimensions and compute the center of the image
#		(h, w) = image.shape[:2]
#		(cX, cY) = (int(w * 0.5), int(h * 0.5))
#       # divide the image into four rectangles/segments (top-left,
#		# top-right, bottom-right, bottom-left)
#		segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),
#			(0, cX, cY, h)]
#       # construct an elliptical mask representing the center of the
#		# image
#		(axesX, axesY) = (int(w * 0.75) / 2, int(h * 0.75) / 2)
#		ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
#		cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)
#       # loop over the segments
#		for (startX, endX, startY, endY) in segments:
#			# construct a mask for each corner of the image, subtracting
#			# the elliptical center from it
#			cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
#			cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
#			cornerMask = cv2.subtract(cornerMask, ellipMask)
# 
#			# extract a color histogram from the image, then update the
#			# feature vector
#			hist = self.histogram(image, cornerMask)
#			features.extend(hist)
#        # extract a color histogram from the elliptical region and
#		# update the feature vector
#		hist = self.histogram(image, ellipMask)
#		features.extend(hist)
 
		# return the feature vector
		return features

	def histogram(self, image, mask):
		# extract a 3D color histogram from the masked region of the
		# image, using the supplied number of bins per channel; then
		# normalize the histogram
		hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,[0, 180, 0, 256, 0, 256])
       #cdf = np.cumsum(hist)
       #hist1 = cdf * hist.max()/ cdf.max()
		#hist1 = cv2.normalize(hist).flatten()
 
		# return the histogram
		return hist
      

