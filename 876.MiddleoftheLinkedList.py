# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tam, cont = 0, 0
        current = head

        if not head:
            return head
        if current.next == None:
            return head
        
        while head:
            tam += 1
            head = head.next
        
        if tam % 2 == 0:
            middle = tam // 2
        else:
            middle = (tam // 2)
        
        while cont < middle - 1:
            current = current.next
            cont += 1
        
        return current.next
        
        
