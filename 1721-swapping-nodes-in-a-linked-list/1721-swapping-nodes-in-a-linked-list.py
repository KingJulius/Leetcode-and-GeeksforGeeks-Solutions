# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        res[k-1], res[-k] = res[-k], res[k-1]
        curr = ListNode(0)
        tmp = curr
        for ele in res:
            tmp.next = ListNode(ele)
            tmp = tmp.next
        return curr.next