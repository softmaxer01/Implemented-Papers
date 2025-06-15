import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms


class AlexNet(nn.Module):
    def __init__(self):
        super(AlexNet, self).__init__()

        self.conv1 = nn.Conv2d(in_channels=1, out_channels=10, kernel_size=5, stride=2)    
        self.maxpool1 = nn.MaxPool2d(kernel_size=2, stride=2)                               

        self.conv2 = nn.Conv2d(in_channels=10, out_channels=30, kernel_size=3, stride=1)   
        self.maxpool2 = nn.MaxPool2d(kernel_size=2, stride=2)                           

        self.conv3 = nn.Conv2d(in_channels=30, out_channels=60, kernel_size=3, stride=1, padding=1) 
        self.maxpool3 = nn.MaxPool2d(kernel_size=2, stride=2)                           

        self.norm = nn.LocalResponseNorm(2)
        self.relu = nn.ReLU()
        self.dropout=nn.Dropout(0.5)
        self.fc1 = nn.Linear(in_features=60*1*1, out_features=256)
        self.fc2 = nn.Linear(in_features=256, out_features=128)
        self.fc3 = nn.Linear(in_features=128, out_features=64)
        self.fc4 = nn.Linear(in_features=64, out_features=10)

    def forward(self, x):
        x = self.maxpool1(self.relu(self.conv1(x)))
        x = self.norm(x)

        x = self.maxpool2(self.relu(self.conv2(x)))
        x = self.norm(x)

        x = self.maxpool3(self.relu(self.conv3(x)))
        x = x.view(x.size(0), -1)

        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.relu(self.fc3(x))
        x = self.fc4(x)
        return x
