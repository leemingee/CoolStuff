'''
Created by Ming Li at 2019-02-19

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # first draft version, not so clean
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        res = 0
        position = 1
        add = 0
        while l1 and l2:
            val1 = l1.val
            val2 = l2.val
            cur = (val1 + val2 + add) % 10
            add = (val1 + val2 + add) // 10
            res += position * (cur)
            position *= 10
            l1 = l1.next
            l2 = l2.next
        if add == 1:
            res += add * position
        while l1:
            res += (l1.val) * position
            position *= 10
            l1 = l1.next
        while l2:
            res += (l2.val) * position
            position *= 10
            l2 = l2.next
        return self.transform(res)
    
    def transform(self, num):
        if num == 0:
            return [0]
        res = []
        while num > 0:
            res.append(num % 10)
            num = num // 10
        return res

    def addTwoNumbers2(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next


if __name__ == '__main__':
    l1 = [1]
    l2 = [1]
    res = Solution().addTwoNumbers(l1, l2)
    print(res)