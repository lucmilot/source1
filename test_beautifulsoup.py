# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 08:25:25 2018

@author: XT21586
"""

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


with open(outfilename1, "r") as f1:
#    html_doc = f1.read() 
    soup = BeautifulSoup(f1, 'html.parser')
    
#print(soup.prettify())

html_tag = soup.html


for child in html_tag.children:
    print(child.file_name)
    
print('DONE')

file_tag = soup.file
print(file_tag)
print(file_tag.contents)
print(len(file_tag.contents))

tt = [print(x,y ) for x,y in enumerate(file_tag.contents)]


type(file_tag.parent)

file_tag_2 = file_tag.next_sibling

file_tag_3 = file_tag_2.next_sibling

print(file_tag_3.file_name)
 
for tag in soup.find_all(re.compile("schema")):
    print(tag.name, tag.parent.file_name)