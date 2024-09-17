# 利用training数据库提取的左右心室于ED和ES期的体积（利用shape特征类的meshvolume特征）来计算左右心室射血分数
# 射血分数计算公式：EF(%)= ((EDV-ESV)*100)/EDV. (because SV= EDV-ESV).

import pandas as pd

docu= [r'training3\result10.csv', r'training3\result11.csv', r'training3\result12.csv', r'training3\result13.csv']
lip1= pd.read_csv(docu[0])
lpl1= lip1.iloc[:, 0]
lip2= pd.read_csv(docu[1])
lpl2= lip2.iloc[:, 0]
lip3= pd.read_csv(docu[2])
lpl3= lip3.iloc[:, 0]
lip4= pd.read_csv(docu[3])
lpl4= lip4.iloc[:, 0]
# print(lpl1)

rvs= pd.DataFrame()
for i in range(1, len(lip1)):
    rvs.loc[i, 0]= ((float(lpl1[i]) - float(lpl2[i])) * 100) / float(lpl1[i])
for i in range(1, len(lip3)):
    rvs.loc[i, 1]= ((float(lpl3[i]) - float(lpl4[i])) * 100) / float(lpl3[i])
# print(rvs)

rvs.to_csv(r'training3\result14.csv')