import pandas as pd
import quandl#Only allows 50 free calls per day.
import math
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import numpy as np

#Data frame.
df = quandl.get('WIKI/GOOGL')

#Update columns in data frame
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

#The column value we're trying to predict.
forecast_col = 'Adj. Close'
#Fill NAN data with a value.
df.fillna(-99999, inplace=True)

#Get the whole number ceiling of the length of the data frame. 0.1 means try to predict up to 1% in the future
forecast_out = int(math.ceil(0.01*len(df)))

#Shift columns negatively. Columns get shifted up.
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

#Features and labels in numpy array. Create an array of everything but labels. Create an array of just labels.
X = np.array(df.drop(['label'], 1))#Features
y = np.array(df['label'])#Labels

#Scale X before feeding into classifier
X = preprocessing.scale(X)
y = np.array(df['label'])

#Set up training data and testing data for our classifier.
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

print(df.head())