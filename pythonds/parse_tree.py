'''
Created by Ming Li at 2/2/2019

Feature: parse tree of the mathematical str, using pythonds package and the most
low level data structure and algorithms

Description: parse tree

based on the materials of http://interactivepython.org/runestone/static/pythonds/index.html
section 6.6 parse tree.

Contact: ming.li2@columbia.edu
'''

'''
idea of parse tree:
for each element in the str:
Using the information from above we can define four rules as follows:
- If the current token is a '(', add a new node as the left child of the current node, 
    and descend to the left child.
- If the current token is in the list ['+','-','/','*'], set the root value of the 
    current node to the operator represented by the current token. 
    Add a new node as the right child of the current node and descend to the right child.
- If the current token is a number, set the root value of the current node to the 
    number and return to the parent.
- If the current token is a ')', go to the parent of the current node.
'''

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree



# we need to keep track of the current node and its parent node, so we are going to use the
# combination of binarytree and stack (to keep track of the parent node)

def parse_tree(str):
    str_split = str.split()
    node_stack = Stack()
    output_tree = BinaryTree('')
    node_stack.push(output_tree)
    current_root = output_tree
    for each_chara in str_split:
        if each_chara == '(':
            # for ( in the string
            current_root.insertLeft('')
            node_stack.push(current_root)
            # we conduct all the operations on the current node, and the output node
            # is just used for store the first node, which is used to output
            current_root = current_root.getLeftChild()
        elif each_chara not in ['+', '-', '*', '/', ')']:
            # a number to be used for calculation
            current_root.setRootVal(int(each_chara))
            current_parent = node_stack.pop()
            current_root = current_parent
        elif each_chara in ['+', '-', '*', '/']:
            # if a operator
            current_root.setRootVal(each_chara)
            current_root.insertRight('')
            node_stack.push(current_root)
            current_root = current_root.getRightChild()
        elif each_chara == ")":
            current_root = node_stack.pop()
        else:
            raise ValueError
    return output_tree

import operator
def evaluate(parsetree):
    opers_dict = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  "/": operator.truediv}
    
    leftC = parsetree.getLeftChild()
    rightC = parsetree.getRightChild()
    
    if leftC and rightC:
        operator_node = opers_dict[parsetree.getRootVal()]
        return operator_node(evaluate(leftC), evaluate(rightC))
    else:
        return parsetree.getRootVal()

def main():
    pt = parse_tree("( ( 10 + 5 ) * 3 )")  # should be 10 5 + 3 *
    pt.postorder()  #defined and explained in the next section
    print(evaluate(pt))
    
if __name__ == '__main__':
    main()
        
            
    
