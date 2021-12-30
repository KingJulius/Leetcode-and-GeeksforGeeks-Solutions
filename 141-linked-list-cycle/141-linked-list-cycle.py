# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        
        ptr1 = head
        
        if ptr1.next == None:
            return False

        ptr2 = head
        
        while ptr2:
            ptr2 = ptr2.next
            if ptr2 != None:
                ptr2 = ptr2.next
            ptr1 = ptr1.next
            if ptr1 == ptr2:
                return True
        return False
        