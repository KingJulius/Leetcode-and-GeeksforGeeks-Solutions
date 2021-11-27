# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def nodeCount(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    
    def nodeRemoval(self, head ,pos):
        if head and pos == 0:
            return head.next
        
        ptr1 = None
        ptr2 = head
        
        while pos>0:
            ptr1 = ptr2
            ptr2 = ptr2.next
            pos = pos - 1
        
        ptr1.next = ptr2.next
        ptr2 = None

        return head
        
            
            
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node_count = self.nodeCount(head)
        #print(node_count)
        pos = node_count - n
        if pos >= 0:
            head = self.nodeRemoval(head, pos)
        else:
            head = None
        return head
        
    