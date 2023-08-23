import pandas as pd
import numpy as np
ser1=pd.Series([10,20,15,3])
ser2=pd.Series([25,10,20,30])
union=pd.Series(np.union1d(ser1,ser2))
intersection=pd.Series(np.intersect1d(ser1,ser2))
notcommon=union[union.isin(intersection)]
print(union)
print(intersection)
print(notcommon)
print(intersection)
