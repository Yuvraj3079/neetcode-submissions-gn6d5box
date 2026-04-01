# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(curr):
            if not curr:
                return 0
            
            leftMax = dfs(curr.left)
            rightMax = dfs(curr.right)

            #ignore -ve values
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #when we are spliting the nodes (left + cur + right)
            splitSum = curr.val + leftMax + rightMax
            self.res = max(self.res, splitSum)
            #when we are not spliting cur + right or cur + left
            currentLeftOrRighSum = curr.val + max(leftMax, rightMax)
            return currentLeftOrRighSum
        dfs(root)

        return self.res


