#!/usr/bin/python

'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False        
        
        return x == self.reverse(x)
        
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        factor = 1
        if x < 0: factor = -1
        if (abs(x) < 10): return x
        x = abs(x)
        shang, yu = divmod(x, 10)
        ret = yu
        
        while shang:
            shang, yu = divmod(shang, 10)
            ret = ret*10 + yu
            
        return factor*(ret if ret <= 2**31-1 else 0)