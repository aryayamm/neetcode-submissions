# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        cur = ListNode()
        ans = cur
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                cur.val = list1.val
                cur.next = ListNode()
                cur = cur.next
                list1 = list1.next
            else:
                cur.val = list2.val
                cur.next = ListNode()
                cur = cur.next
                list2 = list2.next

        if list1 != None:
            while list1 != None:
                cur.val = list1.val
                list1 = list1.next
                if list1 != None:
                    cur.next = ListNode()
                    cur = cur.next
        else:
            while list2 != None:
                cur.val = list2.val
                list2 = list2.next
                if list2 != None:
                    cur.next = ListNode()
                    cur = cur.next

        return ans