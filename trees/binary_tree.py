class BinaryTreeNode:
    """Defines a Tree Node with a value and link to the chile node"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        return
    def add_left(self, node):
        self.left = node
        return
    
    def add_right(self, node):
        self.right = node
        return
    
    