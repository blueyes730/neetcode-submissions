#    [9, 9, 9, 9, 9, 9, 9]
#    [0, 0 ,0 ,9, 9, 9, 9]
# ------------------------
# [1, 0, 0, 0, 9, 9, 9, 8]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode(0)
        curr = ans
        while l1 is not None or l2 is not None:
            if l1 == None:
                num1 = 0
            else:
                num1 = l1.val
            if l2 == None:
                num2 = 0
            else:
                num2 = l2.val

            numsum = num1 + num2 + carry
            curr.next = ListNode(numsum % 10)
            carry = numsum // 10
            curr = curr.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        if carry != 0: curr.next = ListNode(carry)
        return ans.next
