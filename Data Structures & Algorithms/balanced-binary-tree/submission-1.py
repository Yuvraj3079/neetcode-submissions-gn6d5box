# Question: Balanced Binary Tree 
#Given a binary tree, return true if it is height-balanced and false otherwise.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def height(curr):
            if not curr:
                return 0
            
            left = height(curr.left)
            right = height(curr.right)
            #hDiff = abs(left - right)
            if abs(left - right) > 1:
                self.balanced = False 
            
            return 1 + max(left,right)
        
        height(root)
        return self.balanced