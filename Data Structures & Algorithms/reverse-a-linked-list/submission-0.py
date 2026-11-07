# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def do(prev,cur):
            nonlocal head
            if cur == None:
                return prev
            nx = cur.next
            cur.next = prev

            return do(cur, nx)

        return do(None, head)