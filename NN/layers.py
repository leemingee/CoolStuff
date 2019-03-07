# Created by Ming Li at 3/7/2019

# Feature: 

# Description:

# Contact: ming.li2@columbia.edu

from builtins import range
import numpy as np

def affine_forward(x, w, b):
    """
        Computes the forward pass for an affine function.

        The input x has shape (N, d_1, ..., d_k) and contains a minibatch of N
        examples, where each example x[i] has shape (d_1, ..., d_k). We will
        reshape each input into a vector of dimension D = d_1 * ... * d_k, and
        then transform it to an output vector of dimension M.

        Inputs:
        - x: a numpy array containing input data, of shape (N, d_1, ..., d_k)
        - w: a numpy array of weights, of shape (D, M)
        - b: a numpy array of biases, of shape (M,)

        Returns a tuple of:
        - out: output, of shape (N, M)
    """
    x = x.reshape(x.shape[0], np.prod(x.shape[1:]))
    out = np.dot(x, w) + b
    return out

def affine_backforward(dout, x, w, b):
    """
        Computes the backward pass of an affine function.

        Inputs:
        - dout: upstream derivative, of shape (N, M)
        - cache: Tuple of:
          - x: input data, of shape (N, d_1, ... d_k)
          - w: weights, of shape (D, M)
          - b: bias, of shape (M,)

        Returns a tuple of:
        - dx: gradient with respect to x, of shape (N, d1, ..., d_k)
        - dw: gradient with respect to w, of shape (D, M)
        - db: gradient with respect to b, of shape (M,)
    """
    x = x.reshape(x.shape[0], np.prod(x.shape[1:]))
    dx = np.dot(dout, w.T)
    dw = np.dot(w.T, dout)
    db = dout.T.sum(axis=1)
    return dx, dw, db

