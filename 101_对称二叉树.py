#!/usr/bin/python	

'''
对称二叉树    

给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        
        left = []
        right = []
        
        self.travel_left_first(root.left, left)
        self.travel_right_frist(root.right, right)
        #print (left)
        #print (right)
        
        return left == right
        
    def travel_left_first(self, root, trace):
        if root == None: 
            trace.append(None)   
            return
        #print (root.val)
        trace.append(root.val)
        self.travel_left_first(root.left, trace)
        self.travel_left_first(root.right, trace)
    
    
    def travel_right_frist(self, root, trace):
        if root == None: 
            trace.append(None)   
            return
        #print (root.val)
        trace.append(root.val)   
        self.travel_right_frist(root.right, trace)
        self.travel_right_frist(root.left, trace)