# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def count(self, head):
        count = 0
        while head != None:
            count += 1
            head = head.next
        return count
    
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        c = self.count(head)
        
        if c%2 == 1:
            c = (c+1)//2
            while c-1 != 0:
                head = head.next
                c -= 1
            
        else:
            c = c//2
            while c != 0:
                head = head.next
                c -= 1
        
        
        
        return head
            
        