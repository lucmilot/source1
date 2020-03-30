# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 13:30:32 2018

@author: XT21586
"""



import sys
from io import TextIOWrapper, BytesIO

# setup the environment
old_stdout = sys.stdout
sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)

# do some writing (indirectly)
write("blub")

# get output
sys.stdout.seek(0)      # jump to the start
out = sys.stdout.read() # read output

# restore stdout
sys.stdout.close()
sys.stdout = old_stdout

# do stuff with the output
print(out.upper())

print('test')