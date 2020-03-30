# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 05:41:13 2018

@author: XT21586
"""

#--to execute:  python setup_cxfreeze.py build  
#  build is the dictionary were the stufff is put

import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\XT21586\AppData\Local\Continuum\anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\XT21586\AppData\Local\Continuum\anaconda3\tcl\tk8.6'

setup(name = "hello" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("tk_ex2.py")])