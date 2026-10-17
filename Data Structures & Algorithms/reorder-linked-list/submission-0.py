# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        
        dummy=ListNode(-1)
        dummy.next=slow.next
        slow.next=None

        prev=None
        curr=dummy.next

        while curr:
            after=curr.next
            curr.next=prev
            prev=curr
            curr=after

        list1=head
        list2=prev
        temp=list1
        while list1 and list2:
            list1=list1.next
            temp.next=list2
            temp=temp.next
            list2=list2.next
            temp.next=list1
            temp=temp.next

       





            