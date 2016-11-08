# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:14:23 2016

@author: yang
"""

# import the necessary packages
from colordescriptor import ColorDescriptor
from searcher import Searcher
from getGps import GetGPS
import argparse
import cv2
import glob

#print "in search.py"

#python search.py --dataset /media/yang/DATA/Image_Retrive/queries/ --index index.csv --query ./test/ --result-path ./result

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())
 
# initialize the image descriptor
gps = GetGPS('gps_dataset_yang.csv')
original_gpt = gps.getgps()
cd = ColorDescriptor((8, 12, 3))
fea = []
final_fea = {} 
output = open(args["index"], "w")
# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
	# extract the image ID (i.e. the unique filename) from the image
	# path and load the image itself

	imageID = imagePath[imagePath.rfind("/") + 1:]
	print imagePath,"imagePath"
#	print imageID,"imageID"
	image = cv2.imread(imagePath)
#	print image[210,210,1],"pixel"
	#print imageID,"imageID"
	# describe the image
	features = cd.describe(image)
	# write the features to file
	#features = [str(f) for f in features]
	#output.write("%s\n" % (imageID))
	#output.write("%s\n" % (imageID))
	#for f in features:
		#fea.append(f)
		#print f,"fea"
	final_fea[imageID] = features
	print len(final_fea),"shape"
#	print final_fea,"final_fea"  
# load the query image and describe it
output.write("%s;" % ("testing image name"))
output.write("%s\n" % ("training image name")) 
for imagePath1 in glob.glob(args["query"] + "/*.jpg"):
	imageID1 = imagePath1[imagePath1.rfind("/") + 1:]
#	print imageID1
	query = cv2.imread(imagePath1)
	features = cd.describe(query)
 
# perform the search
	searcher = Searcher(args["index"])
	results = searcher.search(features,final_fea)
#print features,"features"
#print results,"result"
# display the query
#	cv2.imshow("Query", query)
#output.write("%s;" % ("testing image name"))
#output.write("%s\n" % ("training image name")) 
# loop over the results
	for (score, resultID) in results:
	# load the result image and display it
		print score,"score",resultID,"resultID"
 		output.write("%s;" % (imageID1))
 		output.write("%s\n" % (resultID))
# 	cv2.imwrite('file1.jpg',image)
#		print original_gpt.index(resultID),"index1"  
		result = cv2.imread(args["dataset"] + "/" + resultID)
#		cv2.imshow("Result", result)
#		cv2.waitKey(3300)