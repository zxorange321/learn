#!/usr/bin/python

'''

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
示例 3:

输入: 218
输出: false

'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: return True
        if n <= 0: return False
 
        
        x = bin(n)
        if n > 0: return not int(x[3:], 2)
        else: return not int(x[4:], 2)
        