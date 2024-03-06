# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next :
            return False
        step1=head
        step2=head.next
        while step1!=step2:
            if not step2 or not step2.next:
                return False
            step1=step1.next
            step2=step2.next.next
        return True
        
