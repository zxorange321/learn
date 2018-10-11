#!/usr/bin/python
'''	
无重复字符的最长子串

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 无重复字符的最长子串是 "abc"，其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 无重复字符的最长子串是 "b"，其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 无重复字符的最长子串是 "wke"，其长度为 3。
     请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串。

'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        tmp_ret = 0
        start = 0
        for i, si in enumerate(s):
            #print (s[start:i])
            findpos = s.find(si, start, i)
            #print (findpos)
            if findpos == -1:
                tmp_ret += 1
            else: 
                ret = max(ret, tmp_ret)
                start = findpos + 1
                tmp_ret = i - start + 1

        #print ("tmp_ret " , tmp_ret)
        #print ("ret " , tmp_ret)
        return max(ret, tmp_ret)