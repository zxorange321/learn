#!/usr/bin/python

'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1==None or l2==None): return l1 or l2
        
        #lmerge = l1 if l1.val < l2.val else l2
        lmerge = ListNode(-1)
        lp1 = l1
        lp2 = l2
        lpm = lmerge
        
        while (lp1 and lp2):
            if lp1.val < lp2.val:
                lpm.next = lp1
                lp1 = lp1.next
                lpm = lpm.next
            else:
                lpm.next = lp2
                lp2 = lp2.next
                lpm = lpm.next
        if lp1 == None: lpm.next = lp2
        else: lpm.next = lp1
        lpm = lmerge.next
        del lmerge
        return lpm
            