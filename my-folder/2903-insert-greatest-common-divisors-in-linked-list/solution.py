# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a

        curr = head
        while curr.next:
            node1, node2 = curr.val, curr.next.val
            curr.next = ListNode(gcd(node1, node2), curr.next)
            curr = curr.next.next
        
        return head

# Time -> O(n * log(min(a, b)))
# Space -> O(n) for gcd ListNodes, O(1) extra
        
