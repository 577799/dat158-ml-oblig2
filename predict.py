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
    new_image = plt.imread("nedlastninger/image.jpg")
    resized_image = resize(new_image, (32,32,3))
    predictions = model.predict(np.array([resized_image]))

#Sort the predictions from least to greatest
    list_index = [0,1,2,3,4,5,6,7,8,9]
    x = predictions
    for i in range(10):
        for j in range(10):
            if x[0][list_index[i]] > x[0][list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    list_predictions = ["","","","","",""]
    classification = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

    for i in range(5):
        str1 = (classification[list_index[i]], ':', round(predictions[0][list_index[i]] * 100, 2), "%")
        list_predictions[i] = str1
        #print(classification[list_index[i]], ':', round(predictions[0][list_index[i]] * 100, 2), '%')

    return  str(list_predictions)
