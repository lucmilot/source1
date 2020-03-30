# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 06:00:29 2018

@author: XT21586
"""

import winreg as winreg
import os, sys, win32gui, win32con

class RegEntry(object):
    def __init__(self,pathx,namex):
        super(RegEntry,self).__init__
        self.path = pathx
        self.name = namex
        try:
            key1 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.path, 0, winreg.KEY_WRITE)   
        except:  # BI_LUM is not there we create it
            print ("the object <"+pathx+"> is being created")
            try:
                self.path = r'Software'
                self.name = r'BI_LUM' 
                self.create_sub_key()
                key1 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.path, 0, winreg.KEY_WRITE) 
            except: 
                print ('bizarre3')  
        self.path = pathx
        self.name = namex
        values = self.list_entry()
        if values is None :
            self.clear_entry()           

    def create_sub_key(self):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.path, 0, winreg.KEY_WRITE)
        winreg.CreateKeyEx(key, self.name, 0, winreg.KEY_WRITE)
        winreg.CloseKey(key)

    def list_entry(self):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.path, 0, winreg.KEY_READ)
        try:
            values = winreg.QueryValueEx(key, self.name)
            winreg.CloseKey(key)
            return values[0]
        except:
            print('xxx')
            return None

    def clear_entry(self):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, self.name, 0, winreg.REG_MULTI_SZ, [])
        winreg.CloseKey(key)
        
    def add_entry(self, hid):
        values = self.list_entry()
        
        if (values is not None) and (hid not in values):
            values.append(hid)
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.path, 0, winreg.KEY_WRITE)
            winreg.SetValueEx(key, self.name, 0, winreg.REG_MULTI_SZ, values)
            winreg.CloseKey(key)


path = r'Software\BI_LUM'
name = "LucTestx3"
tt = RegEntry(path,name)
tt.add_entry('value1xxxx')
tt.add_entry('value2xxxx')
tt.add_entry('value3xxxx')

file_list = tt.list_entry() 
#vv = tt.list_entry()


#tt = None

print('done')




'''
path = r'Software\BI_LUM'
name = "LucTestx3"
tt = RegEntry(path,name)

path = r'Software'
name = "BI_LUM"
tt = RegEntry(path,name)
tt.create_sub_key()

path = r'Software\BI_LUM'
name = "LucTestx3"
tt = RegEntry(path,name)
tt.add_entry('value1xxxx')




tt.create_sub_key()

try:
    

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_WRITE)
winreg.CreateKeyEx(key, name, 0, winreg.KEY_WRITE)
winreg.CloseKey(key)


path = r'Software\BI_LUM\LucTestx3'
try:
    key1 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_WRITE)   
    print('ok')
except:
    print('ttt')

tt = None
tt = RegEntry()

tt.create_sub_key()

x1 = tt.list_entry()

tt.add_entry('tktk3')

x2 = tt.list_entry()

'''