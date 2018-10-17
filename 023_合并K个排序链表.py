#!/usr/bin/python

'''

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

'''

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        dita = [{}, {}] ## [negative, positive]
        
        if len(lists) == 0 or lists==None: return None
        rethead = ListNode(-1)
        retnode = rethead
        
        for i in lists:
            p = i
            while p != None:
                p.val = int(p.val)
                pn = p.next
                p.next = None
                dit = dita[p.val>=0]
                if dit.__contains__(p.val):
                    dit[p.val].append(p)
                else: dit[p.val] = [p]                   
                p = pn
        #print (p)
        
        for dit in dita:
            #print ("max ",max(dit))
            dit_key = sorted(dit)

            for i in dit_key:
                for node in dit[i]:
                    retnode.next = node
                    retnode = retnode.next
        retnode = None             
        retnode = rethead.next
        del rethead
        return retnode