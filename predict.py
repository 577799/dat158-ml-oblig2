import matplotlib as plt
import matplotlib.image as mpimg
import joblib

model = joblib.load('models/model.joblib')

def prediction():
    #data = mpimg.imread('/nedlastninger')
    ##imgplot = 
    # plt.imshow(img)
    pred = model.predict()
