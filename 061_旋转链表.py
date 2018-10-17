#!/usr/bin/python

'''

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None: return None
        if head.next == None or k == 0: return head
        
        n = 0
        p = head
        tail = None
        while p: # get count of linked list
            n += 1
            if p.next == None: tail = p
            p = p.next
            
        print (tail.val)
        print ("n", n)
        rk = n - divmod(k,n)[1]  # 设置导数第几个
        p = head
        for i in range(rk-1): # 找到第 rk个节点
            p = p.next
        print (p.val)
        tail.next = head
        rthead = p.next
        p.next = None
        
        
        return rthead
        