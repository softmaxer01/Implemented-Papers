import torchvision
import torchvision.transforms as transforms
import model
import train 

def main():
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    train_dataset = torchvision.datasets.MNIST(
        root='./data', train=True, download=True, transform=transform
    )
    test_dataset = torchvision.datasets.MNIST(
        root='./data', train=False, download=True, transform=transform
    )
    model_instance = train.MODEL()
    model_instance.fit(train_dataset, epochs=10, batch_size=32)
    model_instance.predict(test_dataset)

if __name__ == "__main__":
    main()

