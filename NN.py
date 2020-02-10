#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

import tensorflow as tf

from tensorflow import feature_column
from tensorflow.keras import layers


# In[2]:


x_train = []
y_trainFourths = []
y_trainEighths = []
with open('./Pi Code/test.csv') as data: 
    reader = csv.reader(data, delimiter = ',')
    a = []
    b = []
    c = []
    d = []
    for row in data:
        arr = np.zeros(shape = (4, 2500,1))
        total = row.split(",")
        for j in range(0, 2500):
            arr[0][j] = float(total[j][2:len(total[j])-5]) / 666.0
            arr[1][j] = float(total[j+2500][2:len(total[j])-5]) / 666.0
            arr[2][j] = float(total[j+5000][2:len(total[j])-5]) / 666.0
            arr[3][j] = float(total[j+7500][2:len(total[j])-5]) / 666.0
        x_train.append(arr)
        y_trainFourths.append(int(total[10001]))
        y_trainEighths.append(int(total[10002]))
        


# In[3]:


x_train = np.array(x_train)
y_trainFourths = np.array(y_trainFourths)
y_trainEighths = np.array(y_trainEighths)

shuffle = np.arange(x_train.shape[0])
np.random.shuffle(shuffle)

x_train = x_train[shuffle]
y_trainFourths = y_trainFourths[shuffle]
y_trainEighths = y_trainEighths[shuffle]

x_test = x_train[527:]
x_train = x_train[:527]
y_testFourths = y_trainFourths[527:]
y_trainFourths = y_trainFourths[:527]
y_testEighths = y_trainEighths[527:]
y_trainEighths = y_trainEighths[:527]


# In[4]:


print(x_train.shape)
print(y_trainFourths.shape)


# In[5]:


model = tf.keras.Sequential([ 
        tf.keras.layers.Conv2D(32, (3,3), padding='same', activation=tf.nn.relu, input_shape=(4, 2500, 1)),
        tf.keras.layers.Conv2D(32, (2,2), padding='same'),
        tf.keras.layers.Flatten(), 
        tf.keras.layers.Dense(128, activation=tf.nn.relu),
        tf.keras.layers.Dense(64, activation=tf.nn.relu),
        tf.keras.layers.Dense(32, activation=tf.nn.relu),
        tf.keras.layers.Dense(16, activation=tf.nn.relu),
        tf.keras.layers.Dense(4, activation=tf.nn.softmax) 
])

#change shape of input to correct


# In[6]:


model.compile(optimizer=tf.keras.optimizers.Adam(0.01),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.summary()


# In[ ]:


history = model.fit(x_train, y_trainFourths, epochs=200, batch_size=2, validation_data=(x_test, y_testFourths))


# In[ ]:


loss = history.history['loss']
plt.plot(loss)
acc = history.history['accuracy']
plt.plot(acc)
val_acc = history.history['val_accuracy']
plt.plot(val_acc)
plt.ylim(0,5)

