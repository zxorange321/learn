#!/usr/bin/python

'''

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

说明：不允许修改给定的链表。

进阶：
你是否可以不用额外空间解决此题？

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dita = {}
        if head == None: return None
        pa = head
        
        while pa != None:
            if dita.__contains__(pa.next): return dita[pa.next]
            dita[pa] = pa
            pa = pa.next
            
        return None