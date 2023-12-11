# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            curr = head
            nxt = head.next
            while nxt:
                if curr.val == nxt.val:
                    nxt = nxt.next
                    curr.next = None
                else:
                    curr.next = nxt
                    nxt = nxt.next
                    curr = curr.next
            return head