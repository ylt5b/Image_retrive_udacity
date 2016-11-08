# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:12:18 2016

@author: yang
"""

import numpy as np

#print "in searcher.py"
class Searcher:
	def __init__(self, indexPath):
		# store our index path
		self.indexPath = indexPath

	def search(self, queryFeatures,final_fea, limit = 3):
		# initialize our dictionary of results
		results = {}

		# open the index file for reading
		with open(self.indexPath) as f:
			# initialize the CSV reader
			#reader = csv.reader(f)

			# loop over the rows in the index
			for row in final_fea:
				# parse out the image ID and features, then compute the
				# chi-squared distance between the features in our index
				# and our query features
				#features = [float(x) for x in row[1:]]
				#print final_fea[row],"fea1"
				d = self.chi2_distance(final_fea[row], queryFeatures)

				# now that we have the distance between the two feature
				# vectors, we can udpate the results dictionary -- the
				# key is the current image ID in the index and the
				# value is the distance we just computed, representing
				# how 'similar' the image in the index is to our query
				results[row] = d

			# close the reader
			f.close()

		# sort our results, so that the smaller distances (i.e. the
		# more relevant images are at the front of the list)
		results = sorted([(v, k) for (k, v) in results.items()])

		# return our (limited) results
		return results[:limit]

	def chi2_distance(self, histA, histB, eps = 1e-10):
		# compute the chi-squared distance
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])

		# return the chi-squared distance
		return d