'''
Created by Ming Li at 2019-02-03

Feature: priority queue implemented by the binary heap

Description:

A priority queue acts like a queue in that you dequeue an item by removing it from the front.

Contact: ming.li2@columbia.edu
'''

# implementation of binary heap (minheap here)
class binaryHeap:
    
    def __init__(self):
        self.heapList = [0]
        self.currentsize = 0
    
    ################## insert method ######################
    
    def insert(self, new_item):
        '''
        log(n) time for insert function
        
        using append and compare with the parent.
        - append to the last, can obtain the complete tree property of heap
        - by comparing with its parent and swap, can re-obtain the heap property
        :param new_item: new item to be insert
        :return: update the of heap
        '''
        self.heapList.append(new_item)
        self.currentsize += 1
        self.percUp(self.currentsize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    ################## delMin method ######################
    
    def delMin(self):
        '''
        del the root first, then fill the place with the last item
        using the percDown to make sure of the Heap property
        :return: heap del the first element
        '''
        pass
    
    def percDown(self, i):
        pass
    
    def minChild(self, i):
        pass
    
    
    ################## insert method ######################
    # using the binary search insert
    def insert_new(self, new_item):
        assert int(new_item) != None, 'can only insert the int type'
        self.heapList =  self.insert_sorted_list(nums = self.heapList, item = new_item)
        self.currentsize += 1
    
    def insert_sorted_list(self, nums, item):
        '''
        as the heap list is sorted except the last one number, then we
        can using binary search to insert it to the right place
        :param currentsize:
        :return:
        '''
        currentsize = len(list)
        left = 0
        right = currentsize - 1 # right index = size - 1 - 1
        while(left < right):
            mid = int((right-left) / 2) + left
            if nums[mid] == item:
                output_idx =  mid
            elif nums[mid] < item:
                left = mid
            else:
                right = mid
        if nums[left] >= item:
            output_idx = left
        elif nums[right] < item:
            output_idx =  right + 1
        else:
            output_idx = right
        return nums.insert(output_idx, item)
                
        
    