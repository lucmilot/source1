# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 08:25:25 2018

@author: XT21586
"""


import re

#s = "123456789123456789"
#matches = re.findall(r'\d{10}', s, overlapped=True)
#for match in matches: print match


tst1 = """
<OrchestrateCode-SQL> Job_Identifier=DSPD24X8_010_Extract_Key_Driver_Job, stg_header=DB_NZ_V2_CRLD_MWB_STN_EVT_BASE_FACT, sql_stmt=
-- [&"BI_Common.ESP_JobID"]
-- Expected Volume: 200K rows
Select distinct
 MWB_KEY
from V2_CRLD_MWB_STN_EVT_BASE_FACT
where MWB_STN_SEQ_NBR is not null and MWB_STN_SEQ_NBR <> -99
  and (DW_CRT_RUN_DT between  \'[&"BI_Extra_Parameters.AdditionalParm_Date_1"]\' and \'[&"BI_Extra_Parameters.AdditionalParm_Date_2"]\'
   or  DW_UPD_RUN_DT between  \'[&"BI_Extra_Parameters.AdditionalParm_Date_1"]\' and \'[&"BI_Extra_Parameters.AdditionalParm_Date_2"]\')
UNION
Select distinct
 MWB_KEY
from V2_IM_MWB_STN_EVT_BASE_FACT
where MWB_STN_SEQ_NBR is not null and MWB_STN_SEQ_NBR <> -99
  and (DW_CRT_RUN_DT between  \'[&"BI_Extra_Parameters.AdditionalParm_Date_1"]\' and \'[&"BI_Extra_Parameters.AdditionalParm_Date_2"]\'
   or  DW_UPD_RUN_DT between  \'[&"BI_Extra_Parameters.AdditionalParm_Date_1"]\' and \'[&"BI_Extra_Parameters.AdditionalParm_Date_2"]\')
<\OrchestrateCode-SQL>
"""

#re_1 = r"^<OrchestrateCode-SQL.OrchestrateCode-SQL>$"
re_0 = r"<OrchestrateCode-SQL>(.*)<\\OrchestrateCode-SQL>"
re_1a = r"V2_CRLD_MWB_STN_EVT_BASE_FACT"
re_1b = r"V2_IM_MWB_STN_EVT_BASE_FACT"
re_0or1 = r"<OrchestrateCode-SQL>(.*("+re_1a+"|"+re_1b+r").*)<\\OrchestrateCode-SQL>"
re_attribute = r"<OrchestrateCode-SQL>(.*(sql_stmt=).*)<\\OrchestrateCode-SQL>"

pattern_1 = re.compile(re_attribute,re.MULTILINE | re.DOTALL)

m = pattern_1.search(tst1)

if m:
    ms = m.groups()
    print (ms)
    print (ms[0])
    print ('Match found: \n', m.group())
    print ('g0', m.group(0))
    print ('g1', m.group(1))
    print ('g2', m.group(2))
else:
    print ('No match')

tt ='xxx'