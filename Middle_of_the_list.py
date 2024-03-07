# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def length_list(self, head):
        length = 0
        itr = head
        while itr:
            length += 1
            itr = itr.next
        return length

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.length_list(head)
        even = length // 2

        if length % 2 == 0:
            itr = 0
            while itr < even:
                head = head.next
                itr += 1
            return head
        else:
            itr = 0
            while itr < even:
                head = head.next
                itr += 1
            return head
