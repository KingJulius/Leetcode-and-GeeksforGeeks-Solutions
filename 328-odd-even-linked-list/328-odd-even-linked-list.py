# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        ptr1, ptr2, head2 = head, head.next, head.next
        
        while ptr2 and ptr2.next:
            ptr1.next = ptr1.next.next
            ptr2.next = ptr2.next.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        ptr1.next = head2
        
        return head
        
        
        
        