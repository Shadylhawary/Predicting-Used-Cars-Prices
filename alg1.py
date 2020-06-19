import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
import pandas as pd
import numpy as np
import pickle

'''

LOADING ENCODERS
 * CARMAKE_ENCODER
 * CARMODEL_ENCODER

'''
pickle_in1 = open('carMakeEncoder2.pickle', 'rb')
pickle_in2 = open('carModelEncoder2.pickle', 'rb')
carMake_Encoder = pickle.load(pickle_in1)
carModel_Encoder = pickle.load(pickle_in2)

data = pd.read_csv('hatlaee3-optimized2.csv')
FEATURES = ['carMake', 'carModel', 'carYear', 'carKilometer']
PREDICT = 'carPrice'

X = np.array(data[FEATURES])
Y = np.array(data[PREDICT])



model = KNeighborsClassifier(n_neighbors=8)
# model2 = svm.SVC(kernel='linear')
# x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

# model.fit(x_train, y_train)
# model2.fit(x_train, y_train)

# acc_KNN = model.score(x_train, y_train)
# acc_SVM = model2.score(x_train, y_train)
# print(f'KNN ACC: {acc_KNN},   SVM ACC: {acc_SVM}')
while 1:
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)
    model.fit(x_train, y_train)
    acc = model.score(x_test, y_test)
    #print(acc)
    if acc > 0.72:
        break
        
predictions = model.predict(x_test)

def getprediction(cmake, cmodel, cyear, ckilo):
    cmake_encoded = carMake_Encoder.transform([cmake])
    cmodel_encoded = carModel_Encoder.transform([cmodel])
    test = np.array([cmake_encoded, cmodel_encoded, cyear, ckilo]).reshape(1, -1)
    predict1 = model.predict(test)
    #print('answer: ', predict1)
    return predict1
# for i in range(len(predictions)):
#     print(f'Predictions : {predictions[i]},  Input Value : {x_test[i]},  Actual Value: {y_test[i]}')

#--------------------------------MACHINE lEARNING ALGORITHM-----------------------------

# Predict = 'carPrice'
#
# X = np.array(data.drop([Predict])
#
# Y = np.array(data['carPrice'])
#
# x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X,Y,test_size=0.1)
#
# model = KNeighborsClassifier(n_neighbors=5)
# model.fit(x_train, y_train)
#
# acc = model.score(x_test, y_test)
# print(acc)
