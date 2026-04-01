# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 1
        
        def inorderTrav(curr, maxSoFar):

            if not curr:
                return 0
            
            if (curr.val >= maxSoFar):
                print(f'count: {self.count} Value: {curr.val} Max: {maxSoFar} ')
                self.count += 1
                maxSoFar = curr.val
            
            inorderTrav(curr.left, maxSoFar)
            inorderTrav(curr.right, maxSoFar)
        if root.left:
            inorderTrav(root.left, root.val)
        if root.right:
            inorderTrav(root.right, root.val)
        return self.count