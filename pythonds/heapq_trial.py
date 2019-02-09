'''
Created by Ming Li at 2019-02-09

Feature: test module for heapq, built in python module implemented heap

Description: 

Contact: ming.li2@columbia.edu
'''

import heapq

'''By default, the heaqp in python is the min heap, not max heap'''

'''to get the usage of the max heap, using heapq.nlargest

heapq.nlargest(n, iterable, key=None)

Return a list with the n largest elements from the dataset defined by iterable.
key, if provided, specifies a function of one argument that is used to extract a
comparison key from each element in iterable (for example, key=str.lower).
Equivalent to: sorted(iterable, key=key, reverse=True)[:n].

'''
some_list = list(range(10, 1, -1))
heapq.heapify(some_list) # in O(n) time


# Heap elements can be tuples.
# This is useful for assigning comparison values (such as task priorities) alongside the main record being tracked:
from heapq import heappush, heappop
h = []
heappush(h, (5, 'write code'))
heappush(h, (7, 'release product'))
heappush(h, (1, 'write spec'))
heappush(h, (3, 'create tests'))
print(heappop(h)) # (1, 'write spec')

'''LC 23, merge k linked list'''
# time should be Nlogk, space should be O(k)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def mergeKLists(self, lists):
        ans = []
        heap = []
        for i in xrange(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, lists[i]))
        while heap:
            top = heapq.heappop(heap)
            ans.append(top[0])
            if top[1].next:
                heapq.heappush(heap, (top[1].next.val, top[1].next))
        return ans

from queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val,node))
        while q.qsize()>0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next