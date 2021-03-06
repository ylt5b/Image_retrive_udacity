# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:07:58 2016

@author: yang
"""

# import the necessary packages
from colordescriptor import ColorDescriptor
import argparse
import glob
import cv2
import numpy as np
 
# construct the argument parser and parse the arguments
np.set_printoptions(threshold='nan')
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())
 
# initialize the color descriptor
cd = ColorDescriptor((8, 12, 3))
# open the output index file for writing
output = open(args["index"], "w")
fea = [] 
# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
	# extract the image ID (i.e. the unique filename) from the image
	# path and load the image itself
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)
 
	# describe the image
	features = cd.describe(image)
	# write the features to file
	#features = [str(f) for f in features]
	output.write("%s\n" % (imageID))
	for f in features:
		fea.append(f)
		print f,"fea"  
		output.write("%s\n" % (f))
	#print fea,"feature"
	#output.write("%s,%s\n" % (imageID, ",".join(features)))
 
# close the index file
output.close()