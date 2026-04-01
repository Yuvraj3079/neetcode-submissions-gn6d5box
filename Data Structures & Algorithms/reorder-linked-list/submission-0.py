# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        cur = sHalf = head
        #iterate till we reach half of the list
        while cur and cur.next:
            cur = cur.next.next
            sHalf = sHalf.next


        prev, cur = None, sHalf
        #reverse the other half
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        newList = ListNode()
        #prev holds the head of reversed LL
        temp, cur = newList, head
        i = 0
        while prev and cur:
            if i % 2 == 0:
                temp.next = cur
                cur = cur.next
            else:
                temp.next = prev
                prev = prev.next
            temp = temp.next
            i += 1
        head = newList.next
        