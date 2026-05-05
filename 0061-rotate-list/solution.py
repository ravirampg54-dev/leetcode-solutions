# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # If list is empty or has one node
        if not head or not head.next or k == 0:
            return head

        # Find length of linked list
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Reduce k if greater than length
        k = k % length

        # If no rotation needed
        if k == 0:
            return head

        # Make linked list circular
        tail.next = head

        # Find new tail
        steps = length - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # New head
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head
