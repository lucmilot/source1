# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 09:19:22 2018

@author: XT21586
"""

import re

input_search_string = "ESP_JobID"

re_attribute = r".*"+input_search_string+r".*"
srch_re_pattern = re.compile(re_attribute,re.MULTILINE | re.DOTALL | re.IGNORECASE)

x = """

SELECT DISTINCT EQP_INIT, EQP_NBR, True AS FoundLeaseEqpRef FROM V1_LEAS_EQP_REF

--#BI_Common.ESP_JobID#
-- Expected : 1.5K records daily

"""

m = srch_re_pattern.search(x)

if m:
    print ("found")
else :
    print ("notfound")
    
    
t1 = "Database\\NETZDEV\\ADMIN.VWBM"

t1 = "Database\\NETZDEV\\VWBM"

t1 = "VWBM"
s1 = t1.split("\\")
s2 = s1[-1].split(".")
s = s2[-1]
print (s)

t1 = "Database\\NETZDEV\\ADMIN.VWBM"
print(t1.split("\\")[-1].split(".")[-1])




table_hit_list=[('a',2),('b',2),('a',1)]

table_hit_list.sort()

[print (x) for (x,y) in table_hit_list]

[print (item1,item2) for (item1,itme2) in [for x in table_hit_list]]


table_list_row = 0
for i,item in table_hit_list:
    worksheet_tab_list.write_



