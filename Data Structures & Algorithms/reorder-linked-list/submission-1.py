# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # valarray = []
        # curr = head

        # while curr != None:
        #     valarray.append(curr.val)
        #     curr = curr.next

        # n = len(valarray) - 1
        # curr = head
        # l, r = 0, n

        # for i in range(n+1):
        #     if i % 2 == 0:
        #         curr.val = valarray[l]
        #         l += 1
        #     else:
        #         curr.val = valarray[r]
        #         r -= 1
        #     curr = curr.next
        
        ###########################################################

        # 1) find middle of linked list

        # use slow and fast pointer
        # fast pointer moves twice
        # slow moves once
        # when fast hits end, slow will be at middle

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow will be at start of middle node

        # 2) reverse second half
        prev, curr = None, slow
        while curr:
            curr.next, curr, prev = prev, curr.next, curr 

        # prev will be the tail

        # 3) merge two sorted lists
        first, second = head, prev
        while first.next and second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        

        