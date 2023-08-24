import pandas as pd

data=pd.read_csv("C:/Users/SPTINT-18/Desktop/dataset/Employee data.csv")
#print(data)

#emp=data[data['gender']=='Female']['salary'].sum
#print(emp)

memp=data[data['gender']=='Female']
memp[memp['salary']>20000].sum
print(memp)
