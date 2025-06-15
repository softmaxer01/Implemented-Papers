from numpy import number
import tensorflow as tf 
from tensorflow import keras 
from tensorflow.keras.models import Sequential




class AlexNet():
    def __init__(self,number_of_classes):
        self.num_classes=number_of_classes
        self.model=Sequential()
        


