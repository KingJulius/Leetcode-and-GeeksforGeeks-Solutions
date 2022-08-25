# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        currA, currB = headA, headB
        if currA is None or currB is None:
            return None
        while currA != currB:
            currA = currA.next
            currB = currB.next
            if currA == currB:
                return currA
            if currA is None:
                currA = headB
            if currB is None:
                currB = headA
        return currA
            