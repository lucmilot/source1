# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 06:55:29 2018

@author: XT21586
"""

import os, sys,subprocess


path = os.getcwd()


subprocess.run("dir")  

output = subprocess.check_output(["dir", ""])

sts = subprocess.call("dir" + " ", shell=True)

subprocess.getoutput('dir ')


subprocess.call('dir ')


C:\Users\XT21586\Documents\document\_DOSSET

os.chdir("C:\\Users\\XT21586\\Documents\\document\\_DOSSET\\")

try:
    retcode = subprocess.call("notepadxx" + "  DWTW06E2.txt", shell=True)
    if retcode < 0:
        print("Child was terminated by signal", -retcode, file=sys.stderr)
    else:
        print("Child returned", retcode, file=sys.stderr)
except OSError as e:
    print("Execution failed:", e, file=sys.stderr)
