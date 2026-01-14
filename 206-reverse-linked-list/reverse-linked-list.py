# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head != None:
            
            tail = None

            while head != None:
                tmp = head.next
                head.next = tail
                tail = head
                head = tmp

            return tail
            
        return head