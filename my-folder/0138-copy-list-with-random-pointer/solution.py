"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        deep_copy = {}  # Creating a hash map

        # Creating new nodes and assigning their values
        temp = head
        while temp:
            deep_copy[temp] = Node(temp.val)
            temp = temp.next

        # Assigning the next and random pointers of each node correctly
        temp = head
        while temp:
            deep_copy[temp].next = deep_copy.get(temp.next)
            deep_copy[temp].random = deep_copy.get(temp.random)
            temp = temp.next
        
        return deep_copy[head]
        
