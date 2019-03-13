#!/usr/bin/python
'''

最长回文子串

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

'''

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        k = len(s)
        if len(s) <= 1: return s
#        start = time.time()
#        p = [[False for i in range(k)] for j in range(k)] #p[i][j] 表示 s[i:j+1]是否为回文串
        olist = [0] * k ## 保存 j-1时刻的是否为回文串
        nlist = [0] * k ## 保存 j时刻的是否为回文串
#        end = time.time()

#        print ("Solution time %f" % (end-start))
        max_str = [1, 0, 1] #len, start, end
        for j in range(0, k):
            for i in range(0, j+1):
                if j-i <= 1: 
                    nlist[i] = (s[i]==s[j])
                else:
                    nlist[i] = (olist[i+1] and (s[i]==s[j]))

                if (nlist[i]) and (max_str[0]<j-i+1): 
                    max_str = [j-i+1, i, j+1]
            olist = nlist
            nlist = [0] * k

        # print (max_str)
        return s[max_str[1]: max_str[2]]