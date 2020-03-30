# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 13:30:32 2018

@author: XT21586
"""

import sys
from contextlib import contextmanager
@contextmanager
def stdout_redirected(new_stdout):
    save_stdout = sys.stdout
    sys.stdout = new_stdout
    try:
        yield None
    finally:
        sys.stdout = save_stdout

filename = 'tata'
with open(filename, "w") as f:
    with stdout_redirected(f):
        print ("Hello world")
        print ("Hello bbbbbbbb  world")        

print('DONE')