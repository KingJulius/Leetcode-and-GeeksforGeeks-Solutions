# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sptr, fptr = head, head
        # Even Condition: Fptr is None
        # Odd Condition: Fptr.nexr is None
        while fptr and fptr.next:
            sptr = sptr.next
            fptr = fptr.next if fptr else None
            fptr = fptr.next if fptr else None
        return sptr
        