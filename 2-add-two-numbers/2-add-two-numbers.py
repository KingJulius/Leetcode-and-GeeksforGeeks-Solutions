# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l3 = ListNode(0)
        l3_tail = l3
        while l1 and l2:
            sum = l1.val + l2.val + carry
            #print(sum)
            if (sum//10 >= 1):
                carry = sum//10
                sum = sum % 10
            else:
                carry = 0
            temp = ListNode(sum)
            l3_tail.next = temp
            l3_tail = l3_tail.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            while l1 or carry:
                if l1 != None:
                    sum = l1.val  + carry
                    #print(sum)
                    if (sum//10 >= 1):
                        carry = sum//10
                        sum = sum % 10
                    else:
                        carry = 0
                    temp = ListNode(sum)
                    l3_tail.next = temp
                    l3_tail = l3_tail.next
                    l1 = l1.next
                else:
                    temp = ListNode(carry)
                    l3_tail.next = temp
                    l3_tail = l3_tail.next
                    break
        elif l2:
            while l2 or carry:
                if l2 != None:
                    sum = l2.val  + carry
                    #print(sum)
                    if (sum//10 >= 1):
                        carry = sum//10
                        sum = sum % 10
                    else:
                        carry = 0
                    temp = ListNode(sum)
                    l3_tail.next = temp
                    l3_tail = l3_tail.next
                    l2 = l2.next
                else:
                    temp = ListNode(carry)
                    l3_tail.next = temp
                    l3_tail = l3_tail.next
                    break
        elif carry:
            temp = ListNode(carry)
            l3_tail.next = temp
            l3_tail = l3_tail.next

 
        l3 = l3.next
        return l3
        