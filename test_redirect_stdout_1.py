# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 13:30:32 2018

@author: XT21586
"""

from io import StringIO
import io

import contextlib
@contextlib.contextmanager
def capture():
    import sys
    oldout,olderr = sys.stdout, sys.stderr
    try:
        out=[StringIO(), StringIO()]
        sys.stdout,sys.stderr = out
        yield out
    finally:
        sys.stdout,sys.stderr = oldout, olderr
        out[0] = out[0].getvalue()
        out[1] = out[1].getvalue()

with capture() as out:
    print ('hi')
    print ('hi2')