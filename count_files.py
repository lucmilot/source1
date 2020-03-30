# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:57:16 2018

@author: XT21586
"""

import glob
import sys
import os

path1 = "C:\\Users\\XT21586\\Documents\\document\\Data Stage\\export\\"

os.chdir(path1)
listofxmlfile = [f for f in glob.glob("*.xml")]

print (len(listofxmlfile))