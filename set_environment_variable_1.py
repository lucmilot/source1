# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 06:00:29 2018

@author: XT21586
"""

import winreg as winreg
import os, sys, win32gui, win32con

class RegEntry(object):
    path = r'Software\BI_LUM'
    name = "LucTestx1"

    def list_entry(self):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.path, 0, winreg.KEY_READ)
        values = winreg.QueryValueEx(key, self.name)
        winreg.CloseKey(key)
        return values[0]

    def clear_entry(self):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, self.name, 0, winreg.REG_MULTI_SZ, [])
        winreg.CloseKey(key)
        
    def delete_entry(self):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.path, 0, winreg.KEY_WRITE)
        winreg.DeleteKeyEx(key, self.name, access=KEY_WOW64_64KEY ,reserved =0)
        winreg.CloseKey(key)

    def add_entry(self, hid):
        values = self.list_entry()

        if hid not in values:
            values.append(hid)
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.path, 0, winreg.KEY_WRITE)
            winreg.SetValueEx(key, self.name, 0, winreg.REG_MULTI_SZ, values)
            winreg.CloseKey(key)


tt = None
tt = RegEntry()

x = tt.list_entry()



tt.add_entry('tktk2')

print (tt.path)



import winreg as wreg
import os, sys, win32gui, win32con



path = r'Software\BI_LUM'
#key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, path,0, wreg.KEY_SET_VALUE)
key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, path,0, wreg.KEY_ALL_ACCESS)

name ='LucTest1'
value = "t1"+u"\x00"+"t2"
wreg.SetValueEx(key, name, 0, REG_MULTI_SZ, value)




name ='LucTest'
wreg.QueryValueEx(key, name)

REG_MULTI_SZ

value = 'ttt'
wreg.SetValueEx(key, name, 0, REG_EXPAND_SZ, value)

wreg.QueryValueEx(key, name)

name ='MainFrame_Lvl1'

wreg.QueryValue(key, name)



wreg.SetValue(key,)


                value = queryValue(key, name) + ';' + value
            if value:
                SetValueEx(key, name, 0, REG_EXPAND_SZ, value)



REG_SZ





wreg.queryValue(key, name)

key.Close()

value = queryValue(key, name) + ';' + value


wreg.SetValue(key,'MainFrame_Lvl1'




path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
key = OpenKey(reg, path, 0, KEY_ALL_ACCESS)
show(key)

import winreg as wreg
import os, sys, win32gui, win32con
path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'


key = wreg.OpenKey(wreg.HKEY_CURRENT_USER,'Software\\Microsoft\\Windows\\CurrentVersion\\Run',wreg.KEY_SET_VALUE)


reg = wreg.ConnectRegistry(None, HKEY_LOCAL_MACHINE)
key = wreg.OpenKey(reg, path, 0, wreg.QueryVALUE('OS'))
#key = wreg.OpenKey(reg, path, 0, KEY_ALL_ACCESS)


with OpenKey(HKEY_LOCAL_MACHINE, "foo") as key:



              
              


tt = wreg.QueryInfoKey(key)

tt = wreg.QueryValue(key,'test')


key1 = 
    
    
path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
key = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, "Software\\TestCompany\\TestProject",0, wreg.KEY_SET_VALUE)


path = r'Software\TestCompany\TestProject'
key = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, path,0, wreg.KEY_SET_VALUE)

wreg.show(key)



def queryValue(key, name):       
    value, type_id = QueryValueEx(key, name)
    return value

def show(key):
    for i in range(1024):                                           
        try:
            n,v,t = EnumValue(key, i)
            print '%s=%s' % (n, v)
        except EnvironmentError:
            break          

def main():
    try:
        path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
        reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        key = OpenKey(reg, path, 0, KEY_ALL_ACCESS)
        
        if len(sys.argv) == 1:
            show(key)
        else:
            name, value = sys.argv[1].split('=')
            if name.upper() == 'PATH':
                value = queryValue(key, name) + ';' + value
            if value:
                SetValueEx(key, name, 0, REG_EXPAND_SZ, value)
            else:
                DeleteValue(key, name)
            
        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')
                            
    except Exception, e:
        print e

    CloseKey(key)    
    CloseKey(reg)
    
if __name__=='__main__':    
    usage = \
"""
Usage:

Show all environment vsarisbles - enver
Add/Modify/Delete environment variable - enver <name>=[value]

If <name> is PATH enver will append the value prefixed with ;

If there is no value enver will delete the <name> environment variable

Note that the current command window will not be affected, 
only new command windows.
"""
    argc = len(sys.argv)
    if argc > 2 or (argc == 2 and sys.argv[1].find('=') == -1):
        print usage
        sys.exit()
        
    main()    
