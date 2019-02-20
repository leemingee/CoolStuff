'''
Created by Ming Li at 2019-02-20

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # TODO use a size k heapq to ensure the order
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        from heapq import heappush, heappop, heapreplace, heapify
        dummy = node = ListNode(0)
        heap = [(head.val, i, head) for i,head in enumerate(lists) if head]
        heapify(heap)
        dummy = ListNode(0)
        curr = dummy
        while heap != []:
            val, i, node = heap[0]
            if not node.next: # exhausted one linked-list
                heappop(heap)
            else:
                heapreplace(heap, (node.next.val, i, node.next))
                # recycling tie-breaker i guarantees uniqueness
            curr.next = node
            curr = curr.next
        return dummy.next


if __name__ == '__main__':
    res = Solution()
    print(res)