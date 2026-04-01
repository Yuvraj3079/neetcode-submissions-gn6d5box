# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        cur = nextP = head

        while nextP and nextP.next:
            cur = cur.next
            nextP = nextP.next.next
            if nextP == cur:
                return True
            

        return False

        