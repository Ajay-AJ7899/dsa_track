# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None : return head
        #using prev current nextt
        prev = None
        curr = head
        while curr is not None:
            nexxt = curr.next #store the next node
            curr.next = prev #reverse the list
            prev = curr #move pointer forward
            curr = nexxt
        return prev