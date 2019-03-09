from __future__ import print_function

import numpy as np

from ecbm4040.layer_funcs import *
from ecbm4040.layer_utils import *

class TwoLayerNet(object):
    """
    A two-layer fully-connected neural network. The net has an input dimension of
    N, a hidden layer dimension of H, and performs classification over C classes.
    We train the network with a softmax loss function and L2 regularization on the
    weight matrices. The network uses a ReLU nonlinearity after the first fully
    connected layer.

    In other words, the network has the following architecture:
    input -> DenseLayer -> AffineLayer -> softmax loss -> output
    Or more detailed,
    input -> affine transform -> ReLU -> affine transform -> softmax -> output

    The outputs of the second fully-connected layer are the scores for each class.
    """

    def __init__(self, input_dim=3072, hidden_dim=200, num_classes=10, reg=0.0, weight_scale=1e-2):
        """
        Inputs:
        - reg: (float) L2 regularization
        - weight_scale: (float) for layer weight initialization
        """
        self.layer1 = DenseLayer(input_dim, hidden_dim, weight_scale=weight_scale)
        self.layer2 = AffineLayer(hidden_dim, num_classes, weight_scale=weight_scale)
        self.reg = reg
        self.v = None

    def loss(self, X, y):
        """
        Calculate the cross-entropy loss and then use backpropogation
        to get gradients wst W,b in each layer.
        
        Inputs:
        - X: input data
        - y: ground truth
        
        Return loss value(float)
        """
        loss = 0.0
        reg = self.reg
        ###################################################
        #TODO: Feedforward                                #
        ###################################################
        # Forward into first layer
        hidden_layer = self.layer1.feedforward(X)
        # Forward into second layer
        scores = self.layer2.feedforward(hidden_layer)
        
        ###################################################
        #TODO: Backpropogation, here is just one dense    #
        #layer, it should be pretty easy                  #
        ###################################################
        loss, dscores = softmax_loss(scores, y)
        # Backprop into second layer
        dX1 = self.layer2.backward(dscores)
        # Backprop into first layer
        self.layer1.backward(dX1)

        ###################################################
        #              END OF YOUR CODE                   #
        ###################################################
        # Add L2 regularization
        square_weights = np.sum(self.layer1.params[0]**2) + np.sum(self.layer2.params[0]**2)
        loss += 0.5*self.reg*square_weights
        return loss

    def step(self, learning_rate=1e-5, optim = 'SGD', momentum = 0.9):
        """
        Use SGD to implement a single-step update to each weight and bias.
        """
        # creates new lists with all parameters and gradients
        layer1, layer2 = self.layer1, self.layer2
        params = layer1.params + layer2.params
        grads = layer1.gradients + layer2.gradients
        
        # Add L2 regularization
        reg = self.reg
        grads = [grad + reg*params[i] for i, grad in enumerate(grads)]
        ###################################################
        #TODO: Use SGD or SGD with momentum to update     #
        #variables in layer1 and layer2                   #
        ###################################################
        if optim == 'SGD':
            params[0] += -learning_rate*grads[0]
            params[1] += -learning_rate*grads[1]
            params[2] += -learning_rate*grads[2]
            params[3] += -learning_rate*grads[3]
    
        if optim == 'momentum':
            if self.v:
                self.v[0] = momentum*self.v[0] - learning_rate*grads[0]
                self.v[1] = momentum*self.v[1] - learning_rate*grads[1]
                self.v[2] = momentum*self.v[2] - learning_rate*grads[2]
                self.v[3] = momentum*self.v[3] - learning_rate*grads[3]
            else:
                self.v = []
                self.v.append(-learning_rate*grads[0])
                self.v.append(-learning_rate*grads[1])
                self.v.append(-learning_rate*grads[2])
                self.v.append(-learning_rate*grads[3])
            
            params[0] += self.v[0]
            params[1] += self.v[1]
            params[2] += self.v[2]
            params[3] += self.v[3]
            
        ###################################################
        #              END OF YOUR CODE                   #
        ###################################################
   
        # update parameters in layers
        layer1.update_layer(params[0:2])
        layer2.update_layer(params[2:4])
        

    def predict(self, X):
        """
        Return the label prediction of input data
        
        Inputs:
        - X: (float) a tensor of shape (N, D)
        
        Returns: 
        - predictions: (int) an array of length N
        """
        predictions = None
        layer1, layer2 = self.layer1, self.layer2
        #######################################################
        #TODO: Remember to use functions in class SoftmaxLayer#
        #######################################################
        hidden_layer = self.layer1.feedforward(X)
        scores = self.layer2.feedforward(hidden_layer)
        predictions = np.argmax(scores, axis = 1)
        
        #######################################################
        #                 END OF YOUR CODE                    #
        #######################################################
        
        return predictions
    
    def check_accuracy(self, X, y):
        """
        Return the classification accuracy of input data
        
        Inputs:
        - X: (float) a tensor of shape (N, D)
        - y: (int) an array of length N. ground truth label 
        Returns: 
        - acc: (float) between 0 and 1
        """
        y_pred = self.predict(X)
        acc = np.mean(np.equal(y, y_pred))
        
        return acc
    
    def save_model(self):
        """
        Save model's parameters, including two layer's W and b and reg
        """
        return [self.layer1.params, self.layer2.params, self.reg]
    
    def update_model(self, new_params):
        """
        Update layers and reg with new parameters
        """
        layer1_params, layer2_params, reg = new_params
        
        self.layer1.update_layer(layer1_params)
        self.layer2.update_layer(layer2_params)
        self.reg = reg
        
        
        


