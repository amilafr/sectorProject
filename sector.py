# import tensorflow as tf
from tensorflow import keras

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from data import *

names = ['k1','k2','k3','k4','k5', 'result']
names2 = list(range(0,len(records3)))
train_data = pd.DataFrame(actual_data, index=names2, columns=names)

X = train_data[['k1', 'k2', 'k3', 'k4', 'k5']]
y = train_data['result']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=1)
# np.random.shuffle(train_data)
# print(train_data)


model = keras.Sequential([
    # hidden layer 1 -> 5 neuron, input layer 5 neuron
    keras.layers.Dense(5, input_shape=(5,), activation='relu'),

    #hidden layer 2
    keras.layers.Dense(5, activation='relu'),
    keras.layers.Dense(5, activation='relu'),
    # keras.layers.Dense(5, activation='relu'),
    # keras.layers.Dense(5, activation='relu'),

    # output layer ada 3 kemungkinan
    keras.layers.Dense(4, activation='sigmoid')
])
# loss function, akurasi
model.compile(optimizer='adam',
              loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

x = np.column_stack((train_data.k1.values,
                     train_data.k2.values,
                     train_data.k3.values,
                     train_data.k4.values,
                     train_data.k5.values))

model.fit(x, train_data.result.values, batch_size=10, epochs=125)
# model.fit(X_train, y_train, batch_size=10, epochs=100)

# test_data = np.
# model.evaluate(X_test, y_test)

# print("Prediction", np.round(model.predict(np.array([[2,2,2,1,3]]))))
# # new instance where we do not know the answer
# Xnew = [3,3,3,3,3]
# # make a prediction
# ynew = model.predict_step(Xnew)
# # show the inputs and predicted outputs
# print("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))
# new instance where we do not know the answer

# Xnew = np.array([[1,1,1,3,1]])
# # make a prediction
# ynew = model.predict(Xnew)
# # show the inputs and predicted outputs
# print("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))

# first_layer_weights = model.layers[0].get_weights()[0]
# first_layer_biases  = model.layers[0].get_weights()[1]
# second_layer_weights = model.layers[1].get_weights()[0]
# second_layer_biases  = model.layers[1].get_weights()[1]

# print(second_layer_biases)
# print(second_layer_weights)

# layer_weights = []
# layer_biases = []
for i in range(0, len(model.layers)):
    print('----- layer ' + str(i+1) + ' -----')
    print('weights')
    print(model.layers[i].get_weights()[0])
    print('biases')
    print(model.layers[i].get_weights()[1])
    print()

testing_data = pd.read_excel('testing.xlsx', sheet_name='Sheet1', header=0)
# testing_data = pd.DataFrame(df, columns= ['Product'])

# print(bobot['K1'])
arr_test = []
for i in range(0,50):
    arr = []
    arr.append(testing_data['K1'][i])
    arr.append(testing_data['K2'][i])
    arr.append(testing_data['K3'][i])
    arr.append(testing_data['K4'][i])
    arr.append(testing_data['K5'][i])
    arr_test.insert(i, arr)

print()
i = 1
for a in arr_test:
    Xnew = np.array([a])
    # make a prediction
    ynew = model.predict(Xnew)
    # show the inputs and predicted outputs
    print(i, " X=%s, Predicted=%s" % (Xnew[0], np.where(ynew[0] == max(ynew[0]))))
    i += 1

