# Created by Ming Li at 3/7/2019

# Feature: 

# Description:

# Contact: ming.li2@columbia.edu
import numpy as np
class relu:

    def __init__(self):
        pass

    def relu_forward(self, x):
        """
        Computes the forward pass for rectified linear units (ReLUs).

        Input:
        - x: inputs, of any shape

        Returns a tuple of:
        - out: output, of the same shape as x
        """
        out = np.maximum(x)
        return out

    def relu_backward(self, dout, x):
        """
        Computes the backward pass for rectified linear units (ReLUs).

        Input:
        - dout: upstream derivatives, of any shape

        Returns:
        - dx: gradient with respect to x
        """
        dx = dout
        dx[dx < 0] = 0
        return dx