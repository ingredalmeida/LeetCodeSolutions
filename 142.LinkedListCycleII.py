# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        visiteds = set()

        while current:
            if current in visiteds:
                return current
            visiteds.add(current)
            current = current.next
        
        return None



        