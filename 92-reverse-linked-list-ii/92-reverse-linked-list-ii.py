# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = ListNode(0, head)
        prev, curr = root, head
        for i in range(left-1):
            prev = curr
            curr = curr.next
        p = None
        for i in range(right-left+1):
            tmp = curr.next
            curr.next = p
            p = curr
            curr = tmp
        prev.next.next = curr
        prev.next = p
        return root.next
