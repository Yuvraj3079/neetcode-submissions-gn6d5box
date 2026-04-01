# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1
        
        dummy = ListNode(0,head)
        prev_group_end = dummy

        while size>=k:

            curr = prev_group_end.next
            prev = None

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            #connect the reversed group with rest of LL
            temp = prev_group_end.next
            prev_group_end.next = prev
            temp.next = curr

            prev_group_end = temp
            size -=k
        return dummy.next
            

