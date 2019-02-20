'''
Created by Ming Li at 2019-02-20

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''

class Solution:
    def isValid(self, s: 'str') -> 'bool':
        reverse_dict = {
            ']': '[', '}': '{', ')': '('
        }
        pre_stack = []
        for each in list(s):
            if each in reverse_dict.keys():
                if len(pre_stack) == 0:
                    return False
                else:
                    pre_each = pre_stack.pop()
                    if pre_each != reverse_dict.get(each):
                        return False
            else:
                pre_stack.append(each)
        if len(pre_stack) != 0:
            return False
        return True

if __name__ == '__main__':
    res = Solution().isValid("{}()[]")
    print(res)