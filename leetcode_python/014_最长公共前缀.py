#!/usr/bin/python

'''
最长公共前缀   

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

'''

 class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1: return ""
        if len(strs) < 2: return strs[0]
        
        str_com = strs[0]
        i = 1
        while (i < len(strs)):
            str_com = min(str_com, self.getCommonPrefix(str_com, strs[i]))
            i += 1
        return str_com
        
        
    def getCommonPrefix(self, str1, str2):
        i = 0
        a = ""
        while (i < len(str1) and i < len(str2)):
            if str1[i] != str2[i]:
                break
            a += str1[i]
            i += 1
        
        return a