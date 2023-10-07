# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        lista1 = []
        while l1:
            lista1.append(l1.val)
            l1 = l1.next

        lista2 = []
        while l2:
            lista2.append(l2.val)
            l2 = l2.next

        lista1_string = list(map(str,lista1))
        lista2_string = list(map(str,lista2))