# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        sptr, fptr = head, head.next
        while fptr and fptr.next:
            sptr = sptr.next
            fptr = fptr.next.next 
        
        second = sptr.next
        prev = sptr.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second  = tmp1, tmp2
        
        
        
        
        
            
        