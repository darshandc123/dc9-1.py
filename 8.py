import pandas as pd
import numpy as np

dict={'first number':[10,20,np.nan,40,50],
      'second number':[np.nan,20,30,40,50],
      'third number':[10,20,30,40,np.nan]}

data=pd.DataFrame(dict)
print(data)
#print(data.isnull())
#print(data.notnull())
#print(data.dropna(how='all'))
#print(data.fillna(10))
#print(data.fillna(method='pad'))
print(data.fillna(method='bfill'))
