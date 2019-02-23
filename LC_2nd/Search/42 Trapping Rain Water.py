'''
Created by Ming Li at 2019-02-22

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        N = len(height)
        left_largest = [0] * N
        left_largest[0] = height[0]
        right_largest = [0] * N
        right_largest[N-1] = height[N-1]
        res = 0
        min_between = [0] * N
        for i in range(1, N, 1):
            left_largest[i] = max(left_largest[i-1], height[i])
        for j in range(N-2, -1, -1):
            right_largest[j] = max(right_largest[j+1], height[j])
        for k in range(N):
            min_between[k] = min(left_largest[k], right_largest[k])
            res += min_between[k] - height[k]
        return res
    
if __name__ == '__main__':
    testcase = [0,1,0,2,1,0,1,3,2,1,2,1]
    res = Solution().trap(height=testcase)
    print(res)