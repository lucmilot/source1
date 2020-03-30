# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 12:46:19 2018

@author: XT21586
"""
import glob
import pprint, pickle
import os
from html.parser import HTMLParser
#import re



class Mapping(dict):
   def __init__(self,*arg,**kw):
      super(Mapping, self).__init__(*arg, **kw)


rc_file_nm = ""
line_cum = ""

sw_columns = False
sw_property = False
property_name = ""
o = None

class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        global sw_columns, sw_property, property_name, o
        #print("Start tag:", tag)
        #f1.write("Start tag:" + tag + "\n")
        
         
        if tag == 'columns':
            sw_columns = True
            o = Mapping()
            o['tag'] = tag
            o['attributes'] = []
            o['property_attributes'] = []
            #print(o)
    
            for attr in attrs:
                ttt = dict([(attr[0],attr[1])])
                print(ttt)
                o['attributes'].append(ttt)
                #print (o)
            #f1.write("     attr:" + "(" + attr[0] +"," + attr[1] + ")\n")
                
        if tag == 'property' and sw_columns == True :  
            sw_property = True
            for attr in attrs:
                #there is only one attribute for property , the loop will be done once
                for attr in attrs:
                    property_name = attr[1]
                #f1.write("     attr:" + "(" + attr[0] +"," + attr[1] + ")\n")       

    def handle_endtag(self, tag):
        global sw_columns, sw_property, property_name, o
        #print("End tag  :", tag)
        f1.write("End tag  :" + tag + "\n")
        if tag == 'columns':
            sw_columns = False 
            pprint.pprint(o)
            pickle.dump(o, outputpkl)
            o = None
        if tag == 'property':
            sw_property = False 


    def handle_data(self, data):
        global sw_columns, sw_property, property_name, o
        #print("Data     :", data)
        f1.write("Data     :" + data + "\n")
        if sw_property == True and sw_columns == True :
            #ttt = dict([(property_name,data)])
            #print(ttt)
            #print(o)
            #print(o['property_attributes'])
            o['property_attributes'].append(dict([(property_name,data)]))
            #print(o)





def search_block(filename):

    print(">>>>>", filename)
    f = open(filename, 'r')
    line_cum = ""
    sw_OrchestrateCode_SQL = False
    sw_columns = False    
    # Looping through the file line by line
    for line in f:
        
        if "<OrchestrateCode_SQL" in line:
            sw_OrchestrateCode_SQL = True  
            line_cum = ""
        if sw_OrchestrateCode_SQL :
            line_cum += line
            if "</OrchestrateCode_SQL>" in line:
                sw_OrchestrateCode_SQL = False 
                yield line_cum
                
        if "<columns" in line:
            sw_columns = True
            line_cum = ""            
        if sw_columns :
            line_cum += line
            if "</columns>" in line:
                sw_columns = False 
                yield line_cum                
    
    yield line_cum   
    line_cum = ""
    sw_OrchestrateCode_SQL = False
    sw_columns = False               
    f.close()


def loadall(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break




path1 = "C:\\Users\\XT21586\\Documents\\document\\Data Stage\\export1\\data_mapping\\"


outfilename1 = path1 + "debug.txt"
outfilpkl = path1 + "pickle1.pkl"
search_string = "MWB_STN_EVT_BASE_FACT"
#search_string = "<property"


parser = MyHTMLParser()


first_tm_sw = True
os.chdir(path1)    

with open(outfilename1, "w") as f1:
    with open(outfilpkl, 'wb') as outputpkl:
        for fname in glob.glob("*.html"): 
            gen1 = search_block(fname)    
            for linex in gen1:
                parser.feed(linex)      
                
                
for obj in loadall(outfilpkl):
    if obj['tag'] == 'columns':
        job_identifier     = [d for diciter in obj['attributes']          for (k,d) in diciter.items() if k == 'job_identifier'][0] 
        column_name        = [d for diciter in obj['property_attributes'] for (k,d) in diciter.items() if k == 'Name'][0]
        table_def          = [d for diciter in obj['property_attributes'] for (k,d) in diciter.items() if k == 'TableDef'][0]         
        column_reference   = [d for diciter in obj['property_attributes'] for (k,d) in diciter.items() if k == 'ColumnReference'][0]      
        column_tuple = (job_identifier, column_name, table_def, column_reference)
        print(column_tuple)

#    print(obj['attributes'][0])
    # process object
    # for the demo we just print
    pprint.pprint(obj)                
