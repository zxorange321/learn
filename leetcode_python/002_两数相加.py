#!/usr/bin/python

'''
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1p = l1
        l2p = l2
        add_next = 0
        add_cur = 0
        lre = ListNode(-1)
        lrep = lre
        is_head = True
        
        while (l1p  or l2p or add_next):
            add_cur = (l1p and l1p.val or 0) + (l2p and l2p.val or 0) + add_next
            add_next = add_cur // 10
            val = int(add_cur % 10)
            
            if is_head:
                lrep.val = val
                is_head = False
            else:
                lrep.next = ListNode(val)
                lrep = lrep.next

            l1p, l2p = l1p and l1p.next, l2p and l2p.next

        
        return lre
        