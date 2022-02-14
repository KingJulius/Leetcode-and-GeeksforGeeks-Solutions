# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tmp = head.next if head else None
        while tmp:
            if tmp == head:
                return True
            tmp = tmp.next
            tmp = tmp.next if tmp else None
            head = head.next
        return False
        