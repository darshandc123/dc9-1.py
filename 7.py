import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-18/Desktop/dataset/titan.csv",)
print(data)
plt.scatter(data['Survived'],data['Age'])
plt.xlabel('Survived')
plt.ylabel('Age')
plt.title("scatter plot")
plt.show()
data['Survived'].value_counts()

plt.plot(data['Age'])
plt.plot(data['Fare'])

plt.xlabel('Survived')
plt.ylabel('Age')
plt.bar(data['Survived'],data['Age'])
plt.show()
plt.hist(data['Fare'])
plt.show()
