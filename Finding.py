
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch




dt = pd.read_excel('Reading.xlsx')
#dt.set_index(['Station'], inplace = True)
dt = dt.replace(r'^\s*$', np.NaN, regex=True)


for station in range(0, len(dt.index)-1):
    
    if dt.isnull().loc[station, 'I.S.']:
        s1 = dt.loc[station, 'B.S.']
    else:
        s1 = dt.loc[station, 'I.S.']
    
    if dt.isnull().loc[(station + 1), 'F.S.']:
        s2 = dt.loc[station + 1, 'I.S.']
    else:
        s2 = dt.loc[station + 1, 'F.S.']
        
    difference = s1 - s2

    if difference > 0:
        dt.loc[station + 1, 'RISE'] = difference
    else:
        dt.loc[station + 1, 'FALL'] = difference
    
    
    dt.loc[station + 1, 'R.L.'] = dt.loc[station, 'R.L.'] + difference
    

dt.to_excel("Solved.xlsx")

plt.plot(dt['Station'], dt['R.L.'])

plt.xlabel('Station', labelpad=10)
plt.ylabel('R.L.', rotation=0, labelpad=10)

plt.yticks(rotation=45)

plt.savefig('Graph.png')
plt.show()
