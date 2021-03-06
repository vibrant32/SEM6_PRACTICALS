# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10XDPce51jtTmklPuJL-9IPV9tmVSHAyB
"""

import pandas as pd
import numpy as np

df=pd.read_csv(r'/content/aaditya(3131).csv')

print(df)

df.isnull()

series = pd.isnull(df["Mathscore"])
df[series]

df.notnull()

series1 = pd.notnull(df["Mathscore"])
df[series1]

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])
newdf=df

df

missing_values = ["Na", "na"]
df = pd.read_csv("aaditya(3131).csv", na_values =
missing_values)
df

ndf=df
ndf.fillna(0)

A_v=df['Mathscore'].mean()
df['Mathscore'].fillna(value=A_v, inplace=True)
df

ndf.replace(to_replace = np.nan, value = -99)

ndf.dropna()

ndf.dropna(how = 'all')

ndf.dropna(axis = 1)

#box plot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("aaditya(3131).csv")

df

col = ['Mathscore', 'Readingscore']
df.boxplot(col)

#skew plot
df=pd.read_csv("aaditya(3131).csv")
from scipy .stats import skew
x=[55,78,65,98,97,60,67,65,83,65]
print(skew(x))

print(skew(x,bias=False))

import pylab as p
x1=np.linspace(-5,5,1000)
y1=1./(np.sqrt(2.*np.pi))*np.exp(-.5*(x1)**2)
print(p.plot(x1,y1,'*'))

#scatterplot
import pandas as pd
import numpy
import matplotlib.pyplot as plot
df=pd.read_csv("aaditya(3131).csv")
x=numpy.random.rand(5)
y=numpy.random.rand(5)
plot.scatter(x,y)

plot.title('Making plots with python')

plot.xlabel('5')

plot.ylabel('5')

plot.show()

