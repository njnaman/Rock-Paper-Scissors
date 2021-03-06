import os
import cv2
import numpy as np
from keras.models import Sequential 
from keras.layers import Dense , MaxPool2D , Flatten
from keras.optimizers import Adam
from keras.applications.densenet import DenseNet121


# Path for getting the data set
DATA_PATH = "/content/drive/My Drive"

shape_to_label = {'rock':np.array([1.,0.,0.,0.]),'paper':np.array([0.,1.,0.,0.]),'scissor':np.array([0.,0.,1.,0.]),'ok':np.array([0.,0.,0.,1.])}

INPUT_SHAPE=(300,300,3)

# Densenet Model for Training
densenet = DenseNet121( input_shape = (INPUT_SHAPE) , weights = 'imagenet' , classes=3 ,include_top = False)
densenet.trainable = True

# Extracting data from given path
def getData():
    dataset=[]
    for dr in os.listdir(DATA_PATH):
        if dr not in ['rock' , 'paper' , 'scissor']:
            continue
        count=0
        lab = shape_to_label[dr]
        for picture in os.listdir( os.path.join(DATA_PATH , dr )):
            path = os.path.join(DATA_PATH , dr + '/' + picture)
            img = cv2.imread(path)
            dataset.append([img , lab])
            count=count+1
            
    return dataset

 # Defining the properties of model
def getModel(base):
    model = Sequential(
        [
            base,
            MaxPool2D(),
            Flatten(),
            Dense(4,activation='softmax')
        ]
    )
    return model

model = getModel(densenet)

model.compile(
    optimizer = Adam(),
    loss = 'categorical_crossentropy',
    metrics = ['acc']
)

data = getData()
imgData , labels = zip(*data)
imgData = np.array(imgData)
labels = np.array(labels)

# Fitting the model according to the given data set
model.fit(
    x = imgData,
    y = labels,
    batch_size = 16,
    epochs = 8
)

# saving the trained model
model.save("/content/drive/My Drive/RPS_MODEL1.h5")
model.save("RPS_MODEL1.h5")
