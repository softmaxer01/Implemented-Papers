import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class ImageLoader():
    def __init__(self):
        (self.x_train,self.y_train),(self.x_test,self.y_test)=mnist.load_data()
        self.x_train=self.x_train.reshape(self.x_train.shape[0],28,28,1)
        self.x_test=self.x_test.reshape(self.x_test.shape[0],28,28,1)
        self.x_train=self.x_train/255
        self.x_test=self.x_test/255
        self.y_train=keras.utils.to_categorical(self.y_train)
        self.y_test=keras.utils.to_categorical(self.y_test)

    def load_batch_data(self,batch_size=32):
        self.batch_size=batch_size
        datagen=ImageDataGenerator()
        self.training_data_gen=datagen.flow(
            self.x_train,self.y_train,
            batch_size=self.batch_size,
            shuffle=True 
            )
        self.testing_data_gen=datagen.flow(
            self.x_test,self.y_test,
            shuffle=False 
           )
        return self.training_data_gen,self.testing_data_gen



