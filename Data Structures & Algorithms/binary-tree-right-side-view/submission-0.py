# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        levelOrder = []
        q = collections.deque()
        q.append(root)
        result = []
        while q:

            level = []

            for _ in range(len(q)):

                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                levelOrder.append(level)
            
            
        for i in range(len(levelOrder)):
            result.append(levelOrder[i][-1])
        #print(result)

        return result

                
            
