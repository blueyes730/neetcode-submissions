# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr != None:
            length += 1
            curr = curr.next
        print(f"list length: {length}")
        remove = length - n
        print(f"remove index: {remove}")
        prev, curr = None, head
        for i in range(remove):
            print(f"prev val: {prev.val if prev else None}")
            print(f"curr val: {curr.val}")
            prev = curr
            curr = curr.next
        
        #curr is at node of the index of removed one
        
        if curr == head: 
            head = head.next
            
        else: prev.next = curr.next if curr.next else None
        
        return head