import tensorflow as tf  
from tensorflow import keras 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.datasets import mnist

class LeNet5():
    def __init__(self):
        self.model=Sequential()
        self.model.add(Conv2D(filters=6,kernel_size=(5,5),strides=(1,1),activation="tanh",input_shape=(28,28,1)))
        self.model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
        self.model.add(Conv2D(filters=16,kernel_size=(5,5),strides=(1,1),activation="tanh"))
        self.model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
        self.model.add(Conv2D(filters=120,kernel_size=(4,4),strides=(1,1),activation="tanh"))
        self.model.add(Flatten())
        self.model.add(Dense(84,activation="tanh"))
        self.model.add(Dense(10,activation="softmax"))
        print(self.model.summary())
        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(0.001),
            loss=tf.keras.losses.categorical_crossentropy,
            metrics=["accuracy"]
        )
        print("model initialization successful")
    
    def fit(self,training_data,test_data,epochs=10):
        self.test_data=test_data 
        self.training_data=training_data
        self.epochs=epochs 
        self.history=self.model.fit(self.training_data,epochs=self.epochs,validation_data=test_data)
        return self.history

    def evaluate(self,test_data):
        self.test_data=test_data
        return self.model.evaluate(self.test_data)
        
