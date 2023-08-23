import pandas as pd

data=pd.read_csv("C:/Users/SPTINT-18/Desktop/dataset/auto-mpg.csv")
#print(data)

#stats = data.describe()
#print(stats)

#car=data[data['cylinders']==8][['car name','cylinders']]
#print(car)

modelyear=data.groupby('model year')['model year'].count()
print(modelyear)
