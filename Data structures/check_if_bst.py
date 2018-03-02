# python3
# partial code

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def trace_bst(arr, node):
    if node == None:
        return
    trace_bst(arr, node.left)
    arr.append(node.data)
    trace_bst(arr, node.right)
    

def checkBST(node):
    arr = []
    trace_bst(arr, node)
    return list(set(arr)) == arr
