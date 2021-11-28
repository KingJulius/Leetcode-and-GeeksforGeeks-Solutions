# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        flag = 0
        curr = head
        ls = []
        
        while curr:
            ls.append(curr.val)
            curr = curr.next
        
        #print(ls)
        #ls2 = ls[:]
        #ls.reverse()
        #print(ls)
        #print(head.val)
        if head:
            rev_head = ListNode(ls[0])
    
        
        for i in range(1, len(ls)):
            temp = ListNode(ls[i])
            temp.next = rev_head
            rev_head = temp
        
        print(ls)         
        #print(ls2)
        
        while head:
            if head.val == rev_head.val:
                head = head.next
                rev_head = rev_head.next
            else:
                flag = 1
                break
        
        if flag == 0:
            return True
        else:
            return False