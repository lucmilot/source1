# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 05:30:12 2018

@author: XT21586
"""

import subprocess

command = ['sftp', 'xt21586@r59s2e5.CN.CA']
#tt = subprocess.Popen(command, stdin=subprocess.PIPE).wait(timeout=10)

tt = subprocess.Popen(command, stdin=subprocess.PIPE)

#exit_codes = [p.wait() for p in tt, p2]
exit_codes = [p.wait() for p in tt]
print(exit_codes)

#subprocess.Popen(command, stdin=subprocess.PIPE) 

#output = tt.check_output('ls',shell = True) 
#print (output)


proc = subprocess.Popen(...)
try:
    outs, errs = proc.communicate(timeout=15)
except TimeoutExpired:
    proc.kill()
    outs, errs = proc.communicate()
    
    
    
    
import subprocess

#This command could have multiple commands separated by a new line \n
some_command = "export PATH=$PATH://server.sample.mo/app/bin \n customupload abc.txt"

p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)

(output, err) = p.communicate()  

#This makes the wait possible
p_status = p.wait()

#This will give you the output of the command being executed
print "Command output: " + output