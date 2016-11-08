# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:13:26 2016

@author: yang
"""

import csv
import numpy as np
import os

class GetGPS:
    def __init__(self,indexPath):
            self.indexPath = indexPath
    
    def getgps(self):
        output = open('gps_data_center_new.csv', "w")
        with open(self.indexPath,'r') as f:
            gpsfea = csv.reader(f, delimiter=',')
            original_pgs = []
            for row in gpsfea:
                folder = row[0].split(os.sep)
                original_pgs = []
                print folder[0], "row"
                if folder[0] =="center":               
                    original_pgs.append(folder[1])
                    original_pgs.append(row[1])
                    original_pgs.append(row[2])
                    original_pgs.append(row[3])
                    output.write("%s\n"%(original_pgs))
#                print gpsfea[row],"gpsfea[row]"
            f.close()
        return original_pgs
            