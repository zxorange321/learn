#!/usr/bin/python

'''

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

'''


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.bsearch(nums, 0, len(nums)-1, target)
        
    def bsearch(self, nums, left, right, target):
        #print ("l,r,m", left, right, (left + right) // 2)
        if left > right : return -1
        if left == right: return left if nums[left] == target else -1
        
        mid = (left + right) // 2
        up = nums[left] < nums[mid] # up 表示当前序列有序，先查找有序列的部分，如果不在，就找旋转了的部分
        if up: 
            if nums[left] <= target and target <= nums[mid]: 
                return self.bsearch(nums, left, mid, target)
            else: return self.bsearch(nums, mid+1, right, target)
        else: 
            if nums[mid+1] <= target and target <= nums[right]: 
                return self.bsearch(nums, mid+1, right, target)
            else: return self.bsearch(nums, left, mid, target)
        