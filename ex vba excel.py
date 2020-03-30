# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:35:55 2018

@author: XT21586
"""


import win32com.client as win32

def openWorkbook(xlapp, xlfile):
    try:        
        xlwb = xlapp.Workbooks(xlfile)            
    except Exception as e:
        try:
            xlwb = xlapp.Workbooks.Open(xlfile)
        except Exception as e:
            print(e)
            xlwb = None                    
    return(xlwb)

try:
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = openWorkbook(excel, "C:\\Users\\XT21586\\Documents\\document\\Data Stage\\result1.xls")
    ws = wb.Worksheets('job') 
    excel.Visible = True

except Exception as e:
    print(e)

finally:
    # RELEASES RESOURCES
    ws = None
    wb = None
    excel = None





'''
outfilxls1 = "C:\\Users\\XT21586\\Documents\\document\\Data Stage\\result1.xls"

excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open(outfilxls1)
#wb.Worksheets("orchestratecode_sql").Activate 

wb.Sheets(3).Activate
excel.Visible = True


ws = wb.Worksheets("columns")


ws.Columns(3).ColumnWidth = 15
ws.Columns(3).WrapText = True

#ws.AutoFilterMode = True

ws.Range("A1").AutoFilter


ws.Visible = True
excel.Visible = True
'''