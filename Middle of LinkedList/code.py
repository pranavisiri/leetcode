# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        tmp=head
        while tmp and tmp.next:
            head=head.next
            tmp=tmp.next.next
        return head