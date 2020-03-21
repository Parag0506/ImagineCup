#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/hrishikeshmane/ChecXray_webapp/blob/master/modelsummary_checxray.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[ ]:


import keras
from keras.applications.densenet import DenseNet121
from keras.layers import Input
from keras.models import Model
from keras.layers import Dense
from keras.optimizers import Adam
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
#from generator import DataGenerator


# In[ ]:




#hyper parameter
input_shape = (224, 224, 3)
train_path = '../datas/info_datas.csv'
test_path = '../datas/info_test_datas.csv'
num_of_class = 1


# In[ ]:


img_in = Input(input_shape)              #input of model 
model = DenseNet121(include_top= False , # remove  the 3 fully-connected layers at the top of the network
                weights='imagenet',      # pre train weight 
                input_tensor= img_in, 
                input_shape= input_shape,
                pooling ='avg') 

x = model.output  
predictions = Dense(num_of_class, activation="sigmoid", name="predictions")(x)    # fuly connected layer for predict class 
model = Model(inputs=img_in, outputs=predictions)


# In[ ]:


model.summary()


# In[ ]:


from keras.models import Sequential
from keras.layers import Dense
from keras.utils.vis_utils import plot_model


# In[ ]:


plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)


# In[ ]:




