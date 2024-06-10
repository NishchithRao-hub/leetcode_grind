# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        new_list = []
        current = head
        max_sum = 0
        while current:
            new_list.append(current.val)
            current = current.next
        
        last = len(new_list)-1
        first = 0
        while first < last:
            max_sum = max(max_sum, new_list[first] + new_list[last])
            first += 1
            last -= 1
        return max_sum
        
