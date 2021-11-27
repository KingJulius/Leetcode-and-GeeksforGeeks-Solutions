# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        ptr1 = l3
        while l1 and l2:
            if l1.val  <= l2.val:
                temp = ListNode(l1.val)
                ptr1.next = temp
                ptr1 = ptr1.next
                l1 = l1.next
            else:
                temp = ListNode(l2.val)
                ptr1.next = temp
                ptr1 = ptr1.next
                l2 = l2.next
                
        while l1:
            temp = ListNode(l1.val)
            ptr1.next = temp
            ptr1 = ptr1.next
            l1 = l1.next
                
        while l2:    
            temp = ListNode(l2.val)
            ptr1.next = temp
            ptr1 = ptr1.next
            l2 = l2.next
        
        
        l3 = l3.next
        
        return l3