class Node:
    def __init__(self, val:str, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    pass

node = Node("root", Node("left", Node("left.left")), Node("right"))