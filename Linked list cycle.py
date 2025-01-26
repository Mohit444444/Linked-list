# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Loop that runs while fast and slow pointer are not
        # None and not equal
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If fast and slow pointer points to the same node,
            # then the cycle is detected
            if slow == fast:
                return True
        return False

        # time O(n)
        # space O(1)