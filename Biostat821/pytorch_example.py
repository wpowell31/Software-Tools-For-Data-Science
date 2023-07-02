"""Pytorch example."""
import numpy as np
import torch
from torch import nn

def autograd_example():
    """Demonstrate autograd."""
    x = torch.tensor(1.0, requires_grad=True)
    w = torch.tensor(5.0, requires_grad=True)
    b = torch.tensor(1.0, requires_grad=True)
    temp = w * x
    y = temp + b
    print(y)

    print(b.grad)
    y.backward()
    print(b.grad)

def loss_fn(true, guess):
    """Mean squared error loss."""
    return torch.sum(torch.pow(true-guess, 2)) / true.shape[0]

def model(x, params):
    return x * params[0] + params[1]

class MyLinear(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(in_features, out_features))
        self.bias = nn.Parameter(torch.randn(out_features))

    def forward(self, input):
        return (input @ self.weight) + self.bias

def gradient_descent_example():
    """Demonstrate gradient descent."""
    N = 100
    D = 1
    x = torch.from_numpy(np.random.rand(N, D).astype("float32"))
    w = torch.tensor(5.0, requires_grad=True)
    b = torch.tensor(1.0, requires_grad=True)
    #y = torch.pow(x, 2.0) * w + b
    y = x * w + b

    # Define model
    model = torch.nn.Sequential(
        torch.nn.Linear(1, 4, bias=True),
        torch.nn.ReLU(),
        torch.nn.Linear(4, 1, bias=True),
    )

    model = MyLinear(1,1)
    loss_fn = torch.nn.MSELoss()

    # train mode
    optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
    for _ in range(2000):
        y_pred = model(x)
        loss = loss_fn(y, y_pred)
        loss.backward(retain_graph=True)   
        optimizer.step()     
        optimizer.zero_grad()
        print(list(model.parameters()), loss)


if __name__ == "__main__":
    #autograd_example()
    gradient_descent_example()
