# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        temp = head
        length = 0

        while temp is not None:
            length += 1
            temp = temp.next

        length -= n

        if length == 0:
            return head.next  # remove head

        while length > 1:
            cur = cur.next
            length -= 1

        cur.next = cur.next.next
        return head
