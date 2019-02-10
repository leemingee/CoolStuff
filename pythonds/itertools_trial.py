'''
Created by Ming Li at 2019-02-09

Feature: python3 built-in module itertools

Description: 

Contact: ming.li2@columbia.edu
'''
import itertools
itertools.accumulate([1,2,3,5,6])
itertools.chain([1,2,3], [4,5,6,7,8])
itertools.chain.from_iterable(['abc', 'defsg', '123'])
itertools.compress(data='abcdef', selectors=[1,0,1,0,1,1])


# combination iterators
itertools.combinations()
itertools.permutations()
itertools.product()
itertools.combinations_with_replacement()