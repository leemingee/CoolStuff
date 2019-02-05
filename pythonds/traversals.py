'''
Created by Ming Li at 2019-02-03

Feature: tree traversals: preorder, inorder, postorder

Description: 

Contact: ming.li2@columbia.edu
'''

'''
preorder root -> left -> right
In a preorder traversal, we visit the root node first,
then recursively do a preorder traversal of the left subtree,
followed by a recursive preorder traversal of the right subtree.

inorder left -> root -> right
In an inorder traversal, we recursively do an inorder traversal on the left subtree,
visit the root node, and finally do a recursive inorder traversal of the right subtree.

postorder left -> right -> root
In a postorder traversal, we recursively do a postorder traversal
of the left subtree and the right subtree
followed by a visit to the root node.

'''

# basic idea of three types of traversal
def preorder(tree):
    '''
    preorder traversal of tree, given any tree node
    :param tree: tree node
    :return: preorder traversal print
    '''
    if tree is not None:
        print(tree.getRootVal())
        print(preorder(tree.getLeftChild()))
        print(preorder(tree.getRightChild()))


def inorder(tree):
    if tree:
        print(inorder(tree.getLeftChild()))
        print(tree.getRootVal())
        print(inorder(tree.getRightChild()))
        

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())
        
# using postorder traversal to evaluate the parse tree:
import operator
def evaluate_postorder_traversal(pt):
    opers_dict = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  "/": operator.truediv}
    num_left, num_right = None, None
    if pt is not None:
        num_left = evaluate_postorder_traversal(pt.getLeftChild())
        num_right = evaluate_postorder_traversal(pt.getRightChild())
        oper = opers_dict.get(pt.getRootVal(), None)
        if oper is not None: # if num_left and num_right:
            return oper(num_left, num_right)
        else:
            return pt.getRootVal()
    
def printexp(tree):
    '''
    print the parse tree with the full form
    :param tree:
    :return:
    '''
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild())+')'
    return sVal