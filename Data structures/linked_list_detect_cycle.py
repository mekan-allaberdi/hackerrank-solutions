"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(node):
    visited = dict()
    while node != None:
        data = node.data
        if visited.get(data, False):
            return True
        visited[data] = True
        node = node.next
    return False
    
