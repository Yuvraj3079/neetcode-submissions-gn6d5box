# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.bToArr = []

        def convertToArray(curr):

            if not curr:
                return None
            
            convertToArray(curr.left)
            self.bToArr.append(curr.val)
            convertToArray(curr.right)
        
        convertToArray(root)
        print(self.bToArr)
        return self.bToArr[k-1]