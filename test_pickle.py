# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 12:46:19 2018

@author: XT21586
"""


class Worker(object):

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def __str__(self):
        string = u'[<Worker> name:%s addr:%s]' %(self.name, self.addr)
        return string




def loadall(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break

items = loadall(myfilename)



import re
from bs4 import BeautifulSoup

path1 = "C:\\Users\\XT21586\\Documents\\document\\Data Stage\\export\\data_mapping\\"

sys.path.append(path) 



outfilename1 = path1 + "debug.txt"
search_string = "MWB_STN_EVT_BASE_FACT"

first_tm_sw = True
os.chdir(path1)    
with open(outfilename1, "w") as f1:
    if first_tm_sw :
        f1.write('<html>\n')
        first_tm_sw = False
    for fname in glob.glob("*.html"):
        with open(fname,'r') as f:
        #file_buf = open(fname).read()
            file_buf = f.read()
            if search_string in file_buf:
                f1.write('<FILE file_name="' + fname + '" >\n') 
                f1.write(file_buf+ "\n")    
                f1.write("</FILE>\n") 
    f1.write('</html>')