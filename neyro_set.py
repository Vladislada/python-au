import numpy as np


def σ(x):
  return 1 / (x + 1)

class Neuron:
  def __init__(self, weights, bias):
    self.w = weights
    self.b = bias

  def feedforward(self, inputs):
    total = np.dot(self.w, inputs) + self.b
    return σ(total)

weights = np.array([1, 2])
bias = 4
n = Neuron(weights, bias)

x = np.array([3, 4])
print(n.feedforward(x))


class Network:
    def __init__(self):
        weights = np.array([0, 1])
        bias = 0

        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)

    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)

        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))

        return out_o1
network = Network()
x = np.array([3, 4])
print(network.feedforward(x))