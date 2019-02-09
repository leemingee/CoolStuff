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

if __name__ == '__main__':
    solu = Solution()
    intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
    print(solu.merge(intervals))


