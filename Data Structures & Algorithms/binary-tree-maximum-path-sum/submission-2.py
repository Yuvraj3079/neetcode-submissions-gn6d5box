# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        def dfs(curr):
            if not curr:
                return (0, float("-inf"))

            leftThrough, leftMax = dfs(curr.left)
            rightThrough, rightMax = dfs(curr.right)

            #ignore -ve values
            leftThrough = max(0,leftThrough)
            rightThrough = max(0,rightThrough)

            #path from either left node (cur + left) or right node (cur + right)
            pathThrough = curr.val + max(leftThrough, rightThrough)

            #path when we split nodes (left + cur + right)
            splitPath = curr.val + leftThrough+ rightThrough

            #Overall path
            overallPath = max(leftMax, rightMax, splitPath)

            return (pathThrough, overallPath)
        return (dfs(root)[1])


