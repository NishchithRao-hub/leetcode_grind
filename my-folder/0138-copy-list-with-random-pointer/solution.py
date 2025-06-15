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
        deepCopy = collections.defaultdict(lambda: Node(0))
        deepCopy[None] = None

        curr = head
        while curr:
            deepCopy[curr].val = curr.val
            deepCopy[curr].next = deepCopy[curr.next]
            deepCopy[curr].random = deepCopy[curr.random]
            curr = curr.next

        return deepCopy[head]
        
