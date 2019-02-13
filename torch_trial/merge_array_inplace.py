'''
Created by Ming Li at 2019-02-13

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''
class Solution:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    def merge(self, nums1, m, nums2, n):
        l1, l2, end = m-1, n-1, m+n-1
        while l1 >= 0 and l2 >= 0:
            if nums2[l2] > nums1[l1]:
                nums1[end] = nums2[l2]
                l2 -= 1
            else:
                nums1[end] = nums1[l1]
                l1 -= 1
            end -= 1
        if l1 < 0: # if nums2 left
            nums1[:l2+1] = nums2[:l2+1]

    def merge1(self, nums1, m, nums2, n):
        m, n = m-1, n-1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[m+n+1] = nums1[m]
                m -= 1
            else:
                nums1[m+n+1] = nums2[n]
                n -= 1
        if n != -1: # nums2 is still left
            nums1[:n+1] = nums2[:n+1]
