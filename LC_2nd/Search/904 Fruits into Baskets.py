'''
Created by Ming Li at 2019-02-19

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


class Solution:
    def totalFruit(self, tree: 'List[int]') -> 'int':
        max_cnt = 0
        if not tree:
            return 0
        i, j = 0, 0
        cur_dict = {}
        while j < len(tree):
            if tree[j] in cur_dict:
                print(cur_dict)
                cur_dict[tree[j]] = cur_dict[tree[j]] + 1
                j += 1
                max_cnt = max(max_cnt, sum(list(cur_dict.values())))
            else:
                print(cur_dict)
                cur_dict[tree[j]] = 1
                if len(cur_dict) > 2:
                    cur_dict.pop(list(cur_dict.keys())[0])
                    i = j - 1
                else:
                    j += 1
                max_cnt = max(max_cnt, sum(list(cur_dict.values())))
        return max_cnt

class Solution2:
    def totalFruit(self, tree):
        ans = i = 0
        count = collections.Counter()
        for j, x in enumerate(tree):
            count[x] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans

if __name__ == '__main__':
    testcase1 = [4,1,1,1,3,1,7,5]
    testcase2 = [1,0,1,4,1,4,1,2,3]
    res = Solution().totalFruit(testcase2)
    print(res)