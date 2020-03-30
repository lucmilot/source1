# This Python file uses the following encoding: utf-8
#import sys
#import platform
#import imp
import datetime


#print("Python EXE : " + sys.executable)
#print("Architecture : " + platform.architecture()[0])

#raw_input("nnPress ENTER to quit")[/sourcecode]

# Open a log file to write to
#
f = open(r'C:\Users\XT21586\Documents\document\DFIT\schedule\test1.log',r'w')

# Write date/time
#
#f.write(time.strftime(‘%x %X’))
f.write("Email received")
f.write("\n")
f.write(str(datetime.datetime.now()))

f.close()

print ('test done')
