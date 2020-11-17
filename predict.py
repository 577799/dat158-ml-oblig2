import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import joblib
import pickle
import tensorflow as tf
from skimage.transform import resize 
import numpy as np
from tensorflow import keras


#model = joblib.load('modeltest/saved_model.pb')
#model = tf.saved_model.load('modeltest')
model = keras.models.load_model("modeltest")

def prediction():
    #data = mpimg.imread('/nedlastninger')
    ##imgplot = 
    # plt.imshow(img)
    new_image = plt.imread("bird.jpg")
    resized_image = resize(new_image, (32,32,3))
    predictions = model.predict(np.array([resized_image]))
    return  str(predictions)
