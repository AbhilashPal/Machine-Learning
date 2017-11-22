import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')



data=pd.read_csv('datasets/train.csv')


#1 print(data.head())

print(data.isnull().sum()) #checking for total null values

# Visalising 1 
"""
f,ax=plt.subplots(1,2,figsize=(18,8))
data['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
ax[0].set_title('Survived')
ax[0].set_ylabel('')
sns.countplot('Survived',data=data,ax=ax[1])
ax[1].set_title('Survived')
plt.show()
"""

# Visualizing 2

print( data.groupby(['Parch','Survived'])['Survived'].count())

f,ax=plt.subplots(1,2,figsize=(18,8))
data[['Parch','Survived']].groupby(['Parch']).mean().plot.bar(ax=ax[0])
ax[0].set_title('Survived vs Parch')
sns.countplot('Parch',hue='Survived',data=data,ax=ax[1])
ax[1].set_title('Parch:Survived vs Dead')
plt.show()
