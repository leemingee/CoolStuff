'''
Created by Ming Li at 2019-02-05

Feature:

Description:

Contact: ming.li2@columbia.edu
'''


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        from collections import deque
        stack = deque()
        stack.append(intervals[0])
        for i in range(1, len(intervals)):
            l, r = intervals[i].start, intervals[i].end
            temp = stack.pop()
            l_before, r_before = temp.start, temp.end
            if l >= r_before:
                stack.append(Interval(l_before, r))
            else:
                stack.append(Interval(l_before, r_before))
        return stack


class Solution_2:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        self.n = n
        self.res = []
        self.generate()
        return self.res
    
    
    def generate(S = '', l_count = 0, r_count = 0):
        if len(S) == 2 * self.n:
            self.res.append(S)
            return
        else:
            if l_count < self.n:
                self.generate(S+'(', l_count+1, r_count)
            if r_count < l_count:
                self.generate(S+')', l_count, r_count + 1)
    

if __name__ == '__main__':
    #solu = Solution()
    #intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
    #print(solu.merge(intervals))
    
    solu2 = Solution_2()
    solu2.generateParenthesis(2)


