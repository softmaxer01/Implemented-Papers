import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import mnist
import model
import dataloading
import plotting

def run_pipeline():
    # Load data
    dataloader = dataloading.ImageLoader()
    train_data, test_data = dataloader.load_batch_data(batch_size=64)

    # Initialize and train model
    lenet = model.LeNet5()
    history = lenet.fit(train_data, test_data, epochs=5)

    # Evaluate model
    test_loss, test_acc = lenet.evaluate(test_data)
    print(f"Test Loss: {test_loss:.4f}")
    print(f"Test Accuracy: {test_acc:.4f}")

    # Plot training and validation loss
    plotting.plotting_graphs(history)

# Entry point
if __name__ == "__main__":
    run_pipeline()

