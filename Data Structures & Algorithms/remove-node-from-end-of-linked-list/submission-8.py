# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        i = 0
        
        size = 0
        while cur:
            size += 1
            cur = cur.next
        if size == 1:
            return None
        if size == 2:
            if n == 1:
                head.next = None
                return head
            else:
                return head.next
        if n == size:
            return head.next

        cur = head

        while cur:
            if i == (size - n - 1):
                break
            cur = cur.next
            i += 1
        if cur.next:
            prev = cur
            cur = cur.next
            nextP = cur.next
            prev.next = nextP
        
        return head
        