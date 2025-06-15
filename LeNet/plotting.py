import matplotlib.pyplot as plt 
class plotting_graphs:
    def __init__(self, history):
        self.history = history
        self.plot_metrics()

    def plot_metrics(self):
        plt.figure(figsize=(10, 5))

        # Subplot 1: Loss vs Val Loss
        plt.subplot(1, 2, 1)
        plt.plot(self.history.history["loss"], label="Train Loss")
        plt.plot(self.history.history["val_loss"], label="Val Loss")
        plt.title("Loss vs Val Loss")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.legend()

        # Subplot 2: Accuracy vs Val Accuracy
        plt.subplot(1, 2, 2)
        plt.plot(self.history.history["accuracy"], label="Train Accuracy")
        plt.plot(self.history.history["val_accuracy"], label="Val Accuracy")
        plt.title("Accuracy vs Val Accuracy")
        plt.xlabel("Epoch")
        plt.ylabel("Accuracy")
        plt.legend()

        plt.tight_layout()
        plt.show()

