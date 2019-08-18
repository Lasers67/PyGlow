from torch import nn
from glow.utils import Activations as A


class Dense(nn.Module):
    """
    Class for full connected dense layer.

    """

    def __init__(self, output_dim, activation=None):
        super(Dense, self).__init__()
        self.output_shape = (output_dim, 1)
        self.activation = activation

    # set the input attribute from previous layers
    def set_input(self, input_shape):
        self.input_shape = input_shape
        # components of the NN are defined here
        print(self.input_shape)
        print(self.output_shape)
        self.weights = nn.Linear(self.input_shape[0], self.output_shape[0])

    def forward(self, x):
        x = A.activation_function(self.weights(x), self.activation)
        return x


class Dropout(nn.Module):
    """
     Class for dropout layer - regularization using noise stablity of output.

    """

    def __init__(self, prob):
        super(Dropout, self).__init__()
        self.prob = prob

    def set_input(self, input_shape):
        self.input_shape = input_shape
        self.output_shape = (input_shape[0], 1)
        self.dropout_layer = nn.Dropout(self.prob)

    def forward(self, x):
        return self.dropout_layer(x)


class Flatten(nn.Module):
    """
    Class for flattening the input shape

    """

    def set_input(self, input_shape):
        self.input_dim = input_shape
        output_dim = 1
        for axis_value in input_shape:
            output_dim = output_dim * axis_value
        self.output_shape = (output_dim, 1)

    def forward(self, x):
        return x.view(x.size(0), -1)
