#!/usr/bin/python

'''

有效的括号   

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

#左括号必须用相同类型的右括号闭合。
#左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        k = 0
        while (k < len(s)):
            if s[k] in "([{":
                stack.append(s[k])
            else: 
                if len(stack) == 0 or self.cmp(stack.pop(),s[k]) == False: return False
               
            k += 1
        
        return len(stack) == 0
    
    def cmp(self, a, b):
        if ((a == '(' and b == ')') or (a == '[' and b == ']') or (a == '{' and b == '}'))  : return True
        return False
                