'''
Created by Ming Li at 2019-02-12

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


def ways_of_climbing_stairs(n):
    # using the recursion
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return ways_of_climbing_stairs(n - 1) + ways_of_climbing_stairs(n - 2)

#####################################################################################
# A program to count the number of ways to reach n'th stair if the person can climb up to m stairs for a given value m
# Recursive function used by countWays
def countWaysUtil(n, m):
    if n <= 1:
        return n
    res = 0
    i = 1
    while i <= m and i <= n:
        res = res + countWaysUtil(n - i, m)
        i = i + 1
    return res


# Returns number of ways to reach s'th stair using DP
def countWays(s, m):
    return countWaysUtil(s + 1, m)

#####################################################################################

def countWaysUtil_DP(n, m):
    res = [0 for x in range(n)]  # Creates list res witth all elements 0
    res[0], res[1] = 1, 1
    
    for i in range(2, n):
        j = 1
        while j <= m and j <= i:
            res[i] = res[i] + res[i - j]
            j = j + 1
    return res[n - 1]


# Returns number of ways to reach s'th stair
def countWays_DP(s, m):
    return countWaysUtil(s + 1, m)

#####################################################################################

def ways_of_climbing_stairs2(n):
    # using DP
    res = [0] * n # the DP table
    res[0] = 1
    res[1] = 2
    for i in range(2, n, 1):
        res[i] = res[i-1] + res[i-2]
    return res[n-1]

if __name__ == '__main__':
    print(ways_of_climbing_stairs2(4))
    print(ways_of_climbing_stairs(4))