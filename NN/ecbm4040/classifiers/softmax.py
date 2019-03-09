import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
    """
      Softmax loss function, naive implementation (with loops)

      Inputs have dimension D, there are C classes, and we operate on minibatches
      of N examples.

      Inputs:
      - W: a numpy array of shape (D, C) containing weights.
      - X: a numpy array of shape (N, D) containing a minibatch of data.
      - y: a numpy array of shape (N,) containing training labels; y[i] = c means
        that X[i] has label c, where 0 <= c < C.
      - reg: (float) regularization strength

      Returns a tuple of:
      - loss: (float) the mean value of loss functions over N examples in minibatch.
      - gradient: gradient wst W, an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    num_train = X.shape[0]
    num_classes = W.shape[1]
    for i in range(num_train):
        scores = X[i, :].dot(W)
        scores -= np.max(scores)
        correct_class_score = scores[y[i]]
        score_sum = np.sum(np.exp(scores))
        p = np.exp(correct_class_score) / score_sum
        loss += -np.log(p)
        
        for j in range(num_classes):
            if j == y[i]:
                dW[:, j] += (np.exp(scores[j]) / score_sum - 1) * X[i, :]
            else:
                dW[:, j] += (np.exp(scores[j]) / score_sum) * X[i, :]
    
    # Average and Regularize
    loss /= num_train
    dW /= num_train
    loss += 0.5 * reg * np.sum(W * W)
    dW +=reg*W
    
    #############################################################################
    #                          END OF YOUR CODE                                 #
    #############################################################################

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    num_train = X.shape[0]
    scores = X.dot(W)
    scores = scores - np.max(scores, axis=1)[:, np.newaxis]
    loss = -np.sum(np.log(np.exp(scores[np.arange(num_train), y]) / np.sum(np.exp(scores), axis=1)))
    loss /= num_train
    loss += 0.5 * reg * np.sum(W * W)
    
    correct = np.zeros_like(scores)
    correct[np.arange(num_train), y] = 1
    dW = X.T.dot(np.exp(scores) / np.sum(np.exp(scores), axis=1, keepdims=True) - correct)
    
    # Average and Regularize
    dW /= num_train
    dW += reg * W
    #############################################################################
    #                          END OF YOUR CODE                                 #
    #############################################################################

    return loss, dW
