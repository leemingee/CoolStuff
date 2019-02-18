'''
Created by Ming Li at 2019-02-17

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''

class Solution:
    def getPermutation(self, n, k):
        import math
        res = [0] * n
        numbers = [x for x in range(1, n + 1)]
        k = k - 1

        i = 0
        while i < n:
            fact = math.factorial(n - 1 - i)
            index = k // fact

            res[i] = numbers[index]
            numbers.pop(index)
            k -= index * fact
            i += 1
        return ''.join([str(x) for x in res])