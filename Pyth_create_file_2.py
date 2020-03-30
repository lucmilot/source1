# This Python file uses the following encoding: utf-8
import os
import subprocess
import datetime

file1 = r'C:\Users\XT21586\Documents\document\DFIT\schedule\test1.log'
file2 = r'C:\Users\XT21586\Documents\document\DFIT\schedule\test2.log'

f = open(file2,r'w')
f.write("Email received")
f.write("\n")
f.write(str(datetime.datetime.now()))
f.close()

print ( file2 + ": created")

if os.path.isfile(file1):
	print (file1 + ': also exist we will delete the 2 control file and run toad process')
	p = subprocess.Popen([r"schtasks", r"/run", r"/tn", r"\export_inport_MATTP_evt"])
	os.remove(file1)
	os.remove(file2)
	
	
	