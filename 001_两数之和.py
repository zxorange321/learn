#!/usr/bin/python
'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''



class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dita = {}
        for i, ni in enumerate(nums):
            if dita.__contains__(target - ni) and dita[target - ni][0] != i:
                return sorted([i, dita[target - ni][0]])
            dita[ni] = (i, target - ni)
            
        return []
		
print (Solution().twoSum([2, 7, 11, 15], 9))