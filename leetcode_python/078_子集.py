# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 00:23:45 2018

@author: Administrator
"""

        
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import copy
        res = []
        
        que = [[ni] for i, ni in enumerate(nums)]
        
        while len(que) != 0:
            tmp = que.pop(0)
            #print (list(tmp.keys()))
            if tmp not in res:
                res.append(tmp)
            for i in range(len(nums)):
                tmpa = copy.deepcopy(tmp)
#                print (tmpa)
                if nums[i] not in tmpa:
                    tmpa.append(nums[i])
                    tmpa.sort()
                    if tmpa not in res:
                        que.append(tmpa)

                    
        res.append([])
        return res
    
print (Solution().subsets([1,2,3,4,5,6,7]))