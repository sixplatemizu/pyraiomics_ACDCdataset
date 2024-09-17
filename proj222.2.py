# 从info.cfg中提取图像相应的分类结果

import os
import re
import pandas as pd

df= pd.DataFrame()

docu= r'database\testing'
for root, dirs, files in os.walk(docu):
    ootp= None
    
    for file in files:
        patl= os.path.join(root, file)
        if patl.endswith('.cfg'):
            ootp= patl
            with open(ootp, 'r') as op:
                ko= op.read()
                mop= r'(Group: )(\w+)'
                sss= re.search(mop, ko)
                # mok= float(res.group(2))
                if sss.group(2) == 'NOR':
                    rut= 1
                elif sss.group(2) == 'MINF':
                    rut= 2
                elif sss.group(2) == 'DCM':
                    rut= 3
                elif sss.group(2) == 'HCM':
                    rut= 4
                elif sss.group(2) == 'RV':
                    rut= 5
                else:
                    pass
                new_row = pd.DataFrame([{'Result': rut}], index=[0])
                df = pd.concat([df, new_row], ignore_index=True)
        else:
            pass
        ootp= None
        
oupu= r'testing\resultsp.csv'
df.to_csv(oupu, index= True)
print('Saved!')