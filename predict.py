import matplotlib as plt
import matplotlib.image as mpimg
import joblib

model = joblib.load('imageRecModel.joblib')

def predict():
    #data = mpimg.imread('/nedlastninger')
    ##imgplot = 
    # plt.imshow(img)
    pred = model.predict()
