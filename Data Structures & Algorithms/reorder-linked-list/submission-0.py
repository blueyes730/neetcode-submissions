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
        
        valarray = []
        curr = head

        while curr != None:
            valarray.append(curr.val)
            curr = curr.next

        n = len(valarray) - 1
        curr = head
        l, r = 0, n

        for i in range(n+1):
            if i % 2 == 0:
                curr.val = valarray[l]
                l += 1
            else:
                curr.val = valarray[r]
                r -= 1
            curr = curr.next
        
        