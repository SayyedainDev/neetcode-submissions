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
        curr=head
        nodes={None:None}
        
        while curr:
            nodes[curr]=Node(curr.val)
            curr=curr.next
        
        curr=head
        while curr:
            Copynode=nodes[curr]
            Copynode.next=nodes[curr.next]
            Copynode.random=nodes[curr.random]
            curr=curr.next

        return nodes[head]
        