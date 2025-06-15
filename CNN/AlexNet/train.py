import torch.optim as optim 
import model
import torch.nn as nn 
from torch.utils.data import DataLoader
import torchvision
import torchvision.transforms as transforms
import torch

class MODEL():
    def __init__(self):
        self.learning_rate = 0.001
        self.alexnet = model.AlexNet()
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.alexnet.parameters(), lr=self.learning_rate)
        self.train_losses, self.test_accuracy = [], []

    def fit(self, x, epochs, batch_size):
        self.epochs = epochs
        self.train_data = x
        self.batch_size = batch_size
        self.train_loader = DataLoader(self.train_data, batch_size=self.batch_size, shuffle=True)

        for epoch in range(self.epochs):
            self.alexnet.train()
            running_loss = 0.0 
            for images, labels in self.train_loader:
                self.optimizer.zero_grad()
                self.output = self.alexnet(images)
                loss = self.criterion(self.output, labels)
                loss.backward()
                self.optimizer.step()
                running_loss += loss.item()

            self.train_losses.append(running_loss / len(self.train_loader))
            print(f"Epoch {epoch+1}/{self.epochs}, Loss: {running_loss / len(self.train_loader)}")

    def predict(self, x):
        self.test_data = x
        self.test_loader = DataLoader(self.test_data, shuffle=False)
        self.alexnet.eval()
        correct, total = 0, 0
        self.y_pred = []

        with torch.no_grad():
            for images, labels in self.test_loader:
                outputs = self.alexnet(images)
                _, predicted = torch.max(outputs.data, 1)
                self.y_pred.append(predicted)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        self.test_accuracy.append(100 * correct / total)
        print(f"Test Accuracy: {100 * correct / total}%")



