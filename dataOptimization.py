import pandas as pd
import numpy as np
import sklearn
from sklearn import preprocessing
import pickle

data = pd.read_csv('hatlaee-dataset3.csv')
data.dropna(subset=['carPrice', 'carKilometer'], inplace=True)
data.reset_index(drop=True, inplace=True)
data['carPrice'].replace(to_replace=",", value="", inplace=True)

data['carPrice'] = [i.replace(',', '') for i in data.carPrice]
data['carKilometer'] = [i.replace(',', '') for i in data.carKilometer]
data['carPrice'] = [int(i) for i in data.carPrice]
data['carKilometer'] = [int(i) for i in data.carKilometer]

carModel_Encoder = preprocessing.LabelEncoder()
carMake_Encoder = preprocessing.LabelEncoder()

carModel_Encoder.fit(data['carModel'])
data['carModel'] = carModel_Encoder.fit_transform(data['carModel'])
carMake_Encoder.fit(data['carMake'])
data['carMake'] = carMake_Encoder.fit_transform(data['carMake'])

with open('carModelEncoder2.pickle', 'wb') as f:
    pickle.dump(carModel_Encoder, f)

with open('carMakeEncoder2.pickle', 'wb') as f:
    pickle.dump(carMake_Encoder, f)

def classifier(intCol, toCol):
    '''
    :parameter intCol input an int type column to preform the classification process
    :parameter toCol refers to what columns wants to apply to
    :returns: a classified version of the input column
    '''

    for i, k in enumerate(intCol, start=0):
        if k < 100000:
            data.loc[i, toCol] = 0
        if 150000 > k >= 100000:
            data.loc[i, toCol] = 1
        if 200000 > k >= 150000:
            data.loc[i, toCol] = 2
        if 250000 > k >= 200000:
            data.loc[i, toCol] = 3
        if 300000 > k >= 250000:
            data.loc[i, toCol] = 4
        if 350000 > k >= 300000:
            data.loc[i, toCol] = 5
        if 400000 > k >= 350000:
            data.loc[i, toCol] = 6
        if 450000 > k >= 400000:
            data.loc[i, toCol] = 7
        if 500000 > k >= 450000:
            data.loc[i, toCol] = 8
        if 550000 > k >= 500000:
            data.loc[i, toCol] = 9
        if 600000 > k >= 550000:
            data.loc[i, toCol] = 10
        if 650000 > k >= 600000:
            data.loc[i, toCol] = 11
        if 700000 > k >= 650000:
            data.loc[i, toCol] = 12
        if 750000 > k >= 700000:
            data.loc[i, toCol] = 13
        if 800000 > k >= 750000:
            data.loc[i, toCol] = 14
        if 850000 > k >= 800000:
            data.loc[i, toCol] = 15
        if 900000> k >= 850000:
            data.loc[i, toCol] = 16
        if 1000000 > k >= 900000:
            data.loc[i, toCol] = 17
        if 1200000 > k >= 1000000:
            data.loc[i, toCol] = 18
        if k >= 1200000:
            data.loc[i, toCol] = 19


classifier(data.carPrice, 'carPrice')
classifier(data.carKilometer, 'carKilometer')
data.to_csv('hatlaee3-optimized2.csv')
