import pandas as pd 
import numpy as np
import os 
import matplotlib.pyplot as plt
import seaborn as sns
# Standardize features by removing the mean and scaling to unit variance.
from sklearn.preprocessing import StandardScaler  

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',
                header=None)

df.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash',
    'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols',
    'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines',
    'Proline']

df.head()

X = df.drop(labels='Class label', axis=1)
y = df['Class label']


