'''
Created by Ming Li at 2019-01-30

Feature: Random forest

Description: random forest based on the decision tree

Contact: ming.li2@columbia.edu

Note:
here we use a matrix to store the prediction result for every pair of
tree and data point, we store them in the predicted_matrix
predicted_matrix, each row is each data point, each column is each tree prediction for all data points


predicted_matrix[:, i]
    get access for each column
for each_row in predicted_matrix
    get access for each row

'''

import numpy as np
from decision_tree import ClassificationTree
from utils_RF import get_random_subsets
import pickle
import progressbar

bar_widgets = [
    'Training: ', progressbar.Percentage(), ' ', progressbar.Bar(marker="-", left="[", right="]"),
    ' ', progressbar.ETA()
]
# TODO replace it with tqdm
# from tqdm import tqdm


class RandomForest:
    
    def __init__(self, n_estimators=100, max_features=None, min_samples_split=2,
                 min_gain=0, max_depth=float("inf")):
        '''
        
        :param n_estimators: number of trees
        :param max_features: number of features for each tree generation, maxmium number of features
        :param min_samples_split: used for decision tree split, param for decision tree
        :param min_gain: Minimum information gain req. to continue, param for decision tree
        :param max_depth: Maximum depth for tree, param for decision tree
        '''
        self.n_estimators = n_estimators
        self.max_features = max_features
        self.min_samples_split = min_samples_split
        self.min_gain = min_gain
        self.max_depth = max_depth
        self.progressbar = progressbar.ProgressBar(widgets=bar_widgets)
        self.trees_feature_idx = []
        
        self.trees = [] # initial the list of trees
        for _ in self.n_estimators:
            self.trees.append(
                ClassificationTree(
                    min_samples_split=self.min_samples_split,
                    min_impurity=min_gain,
                    max_depth=self.max_depth
                )
            )
        
    
    def fit(self, X, y):
        '''
        fit the dataset using X, y
        #### process:
        1. choose a subset of dataset
        2. for each dataset, choose a subset of features
        3. using the features of subset data for fitting the decision tree classifier
        :param X:
        :param y:
        :return:
        '''
        n_features = X.shape[1]
        # default, using the sqrt(n_features) for each tree generation
        n_subset_features = np.sqrt(n_features)
        '''get the subset of data points for each tree'''
        subsets = get_random_subsets(X, y, self.n_estimators)
        '''fit each tree'''
        for i in self.progressbar(range(self.n_estimators)):
            '''for each subset of the dataset'''
            X_subset, y_subset = subsets[i]
            '''get a subset of features number n_subset_features'''
            feature_idx = np.random.randint(range(n_features), size=n_subset_features, replace=False)
            '''store the subset of features for each tree'''
            self.trees_feature_idx[i] = feature_idx
            '''fit the single tree classifier'''
            self.trees[i].fit(X_subset[:, feature_idx], y_subset)
        
        '''store the filled trees'''
        TREES_STORE = open('fitted_trees.pickle', 'w')
        pickle.dump(self.trees, TREES_STORE)
        TREES_STORE.close()


    def predict(self, X_new):
        '''
        predict based on the fitted trees, using the X_new
        :param X_new: X_new
        :return: predicted class
        
        Note: here we use a matrix to store the prediction result for every pair of
        tree and data point, we store them in the predicted_matrix
        predicted_matrix, each row is each data point, each column is each tree prediction for all data points
        
        predicted_matrix[:, i] get access for each column
        for each_row in predicted_matrix get access for each row
        '''
        # assert X_new.shape[1] == X.shape[1]
        predicted_matrix = np.zeros(shape=(X_new.shape[0], self.n_estimators))
        for i, tree in enumerate(self.trees):
            feature_idx = self.trees_feature_idx[i]
            # get the prediction for the whole dataset using one tree
            prediction = tree.predict(X_new[:, feature_idx])
            predicted_matrix[:, i] = prediction
        
        y_pred = []
        for predicted_sample_result in predicted_matrix:
            y_pred.append(np.bincount(predicted_sample_result.astype('int')).argmax())
        return y_pred

    
from sklearn import datasets
from sklearn.model_selection import train_test_split

class Test:
    def __init__(self):
        data = datasets.load_digits()
        self.X = data.data
        self.y = data.target

    def test_fit(self, n_estimators):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, seed=2)
        clf = RandomForest(n_estimators=n_estimators)
        clf.fit(X_train, y_train)
    
    def test_predict(self, n_estimators):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3)
        clf = RandomForest(n_estimators=n_estimators)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        print(y_pred)
    
  
def predict_demo(X_new, n_estimators):
    '''
    predict demo for RF, from storing the output to the predicted class
    :param X_new: X_new
    :param n_estimators: n_estimator
    :return: predicted class
    '''
    # assert X_new.shape[1] == X.shape[1]
    predicted_matrix = np.zeros(shape=(X_new.shape[0], n_estimators))
    for i, tree in enumerate(range(n_estimators)):
        prediction = np.random.randint(i+1, size=X_new.shape[0])
        predicted_matrix[:, i] = prediction
        # print(i, predicted_matrix[:, i])

    y_pred = []
    for predicted_sample_result in predicted_matrix:
        # for each_row in predicted_matrix
        # y_pred.append(np.bincount(predicted_sample_result.astype('int')).argmax())
        predicted_for_sample_bincount = np.bincount(predicted_sample_result.astype(np.int))
        y_pred.append(np.argmax(predicted_for_sample_bincount))
    return predicted_matrix, y_pred

def main():
    #test = Test()
    #test.test_predict(n_estimators=10)
    X_new = np.random.rand(10, 5)
    predicted_matrix = predict_demo(X_new, n_estimators=7)
    print(predicted_matrix)
    
if __name__ == '__main__':
    main()