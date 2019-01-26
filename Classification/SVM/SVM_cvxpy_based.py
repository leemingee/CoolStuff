'''
Created by Ming Li at 2019-01-25

Feature: 

Description:
Reference Link:
http://ecomunsing.com/build-your-own-support-vector-machine

Contact: ming.li2@columbia.edu
'''

import numpy as np
import matplotlib.pyplot as plt
import cvxpy
from cvxpy import *
from sklearn.datasets import make_blobs

def create_dataset(n_samples):
    X, y = make_blobs(n_samples=n_samples, centers=2, n_features=2,
                      random_state=0)
    X1 = X[y == 0]
    X2 = X[y == 1]
    return X1, X2, y

X1, X2, y = create_dataset(100)
# the true nums of sample
m = np.sum(y == 0, dtype='int')
n = np.sum(y == 1, dtype='int')

def viz_raw(X1, X2):
    plt.scatter(X1[:,0],X1[:,1])
    plt.scatter(X2[:,0],X2[:,1], color = 'red')
    plt.show()

# optim using cvxpy
d = 2 # where d is the dimension of this problem
a = Variable(d)
b = Variable()
t = Variable()

obj = Maximize(t)

x1_constraints = [a.T * X1[i] - b >= t  for i in range(m)]
x2_constraints = [a.T * X2[i] - b <= -t for i in range(n)]

constraints = x1_constraints +  x2_constraints + [norm(a,2) <= 1]

prob = Problem(obj, constraints)

prob.solve()
print("Problem Status: %s"%prob.status)


## Define a helper function for plotting the results, the decision plane, and the supporting planes

def plotClusters(x,y,a,b,t):
    # Takes in a set of datapoints x and y for two clusters,
    #  the hyperplane separating them in the form a'x -b = 0,
    #  and a slab half-width t
    d1_min = np.min([x[:,0],y[:,0]])
    d1_max = np.max([x[:,0],y[:,0]])
    # Line form: (-a[0] * x - b ) / a[1]
    d2_atD1min = (-a[0]*d1_min + b ) / a[1]
    d2_atD1max = (-a[0]*d1_max + b ) / a[1]

    sup_up_atD1min = (-a[0]*d1_min + b + t ) / a[1]
    sup_up_atD1max = (-a[0]*d1_max + b + t ) / a[1]
    sup_dn_atD1min = (-a[0]*d1_min + b - t ) / a[1]
    sup_dn_atD1max = (-a[0]*d1_max + b - t ) / a[1]

    # Plot the clusters!
    plt.scatter(x[:,0],x[:,1],color='blue')
    plt.scatter(y[:,0],y[:,1],color='red')
    plt.plot([d1_min,d1_max],[d2_atD1min[0,0],d2_atD1max[0,0]],color='black')
    plt.plot([d1_min,d1_max],[sup_up_atD1min[0,0],sup_up_atD1max[0,0]],'--',color='gray')
    plt.plot([d1_min,d1_max],[sup_dn_atD1min[0,0],sup_dn_atD1max[0,0]],'--',color='gray')
    plt.ylim([np.floor(np.min([x[:,1],y[:,1]])),np.ceil(np.max([x[:,1],y[:,1]]))])
    plt.show()
    


plotClusters(X1,X2,a.value,b.value,t)