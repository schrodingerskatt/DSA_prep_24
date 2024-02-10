# Problem Link : https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        temp = l3
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1 is not None:
                sum+=l1.val
                l1 = l1.next
            if l2 is not None:
                sum+=l2.val
                l2 = l2.next
            sum+=carry
            carry = sum//10
            nodeval = ListNode(sum%10)
            temp.next = nodeval
            temp = temp.next
        return l3.next
