# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:57:16 2018

@author: XT21586
"""

import glob
import sys
import os
import re

xx = sorted(os.environ.keys())


path1 = "C:\\Users\\XT21586\\Documents\\document\\Data Stage\\export\\data_mapping\\"



tst1 = """<OrchestrateCode-SQL Job_Identifier=DSPD24X8_010_Extract_Key_Driver_Job, stg_header=DB_NZ_V2_CRLD_MWB_STN_EVT_BASE_FACT, sql_stmt=
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
\OrchestrateCode-SQL>
"""

re_1 = r"<OrchestrateCode-SQL"
pattern_1 = re.compile(re_1)

m = pattern_1.match(tst1)

if m:
    print ('Match found: ', m.group())
else:
    print ('No match')

tt ='xxx'


os.chdir(path1)
listofxmlfile = [f for f in glob.glob("*.xml")]

outfile = path1 + "srchres.txt"
if os.path.exists(outfile):
   os.remove(outfile)

search_string = "MWB_STN_EVT_BASE_FACT"

re_1 = r"<OrchestrateCode-SQL(.+?)OrchestrateCode-SQL>"
pattern_1 = re.compile(re_1)


with open(outfile, "w") as f1:
    for f in glob.glob("*.txt"):
        file_buf = open(f).read()
        if search_string in file_buf:
            txtf_list=re.findall(pattern_1,file_buf)      
            tt=len(txtf_list)
            tt1 = str(tt)
            f1.write(search_string + tt1 + "\n")            
            
#            f1.write(f+"\n")

print("done")
