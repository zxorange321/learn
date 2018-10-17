#!/usr/bin/python

'''

给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。

'''

class Solution(object):
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