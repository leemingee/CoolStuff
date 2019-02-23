'''
Created by Ming Li at 2019-02-22

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''
#TODO too long to read

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        T = [[0] * (1 << 7) for _ in xrange(1 << 7)]
        for triple in allowed:
            u, v, w = (1 << (ord(x) - ord('A')) for x in triple)
            for b1 in xrange(1 << 7):
                if u & b1:
                    for b2 in xrange(1 << 7):
                        if v & b2:
                            T[b1][b2] |= w

        state = [1 << (ord(x) - ord('A')) for x in bottom]
        while len(state) > 1:
            for i in xrange(len(state) - 1):
                state[i] = T[state[i]][state[i+1]]
            state.pop()
        return bool(state[0])

if __name__ == '__main__':
    res = Solution()
    print(res)