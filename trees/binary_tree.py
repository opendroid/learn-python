class BinaryTreeNode:
    """Defines a Tree Node with a value and link to the chile node"""

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        return

    def left(self, left):
        self.left = left
        return

    def right(self, right):
        self.right = right
        return


class BinaryTree:
    def __init__(self, root: BinaryTreeNode) -> None:
        self.root = root
        self.preorder = []
        self.postorder = []
        self.inorder = []
        return

    def pre_order(self, node):
        """Pre -> before children"""
        if node is None:
            return

        self.preorder.append(node.value)
        self.pre_order(node.left)
        self.pre_order(node.right)
        return

    def pre_order_stack(self, root):
        stack = [root]
        self.pre_order = []
        while stack:
            curr = stack.pop()
            self.pre_order.append(curr.value)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return

    def post_order(self, node):
        """Post -> after children"""
        if node is None:
            return

        self.post_order(node.left)
        self.post_order(node.right)
        self.postorder.append(node.value)
        return

    def in_order(self, node):
        """In -> in the middle of children"""
        if node is None:
            return
        self.in_order(node.left)
        self.inorder.append(node.value)
        self.in_order(node.right)
        return

    def in_order_stack(self, root):
        stack = []
        curr = root
        self.inorder = []

        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                self.inorder.append(curr.value)
                curr = curr.right
            else:
                break
        return


def create_a_binary_tree():
    """Example tree
                           100
                         /    \\
                      90       120
                     /  \\     / \\
                    70  80  110  130
                        / \\      / \\
                       50  60   125 140
                           /          \\
                          65          145
                                        \\
                                         150
    """
    n50 = BinaryTreeNode(50)
    n65 = BinaryTreeNode(65)
    n60 = BinaryTreeNode(60, left=n65)
    n70 = BinaryTreeNode(70)
    n80 = BinaryTreeNode(80, n50, n60)
    n90 = BinaryTreeNode(90, n70, n80)
    n125 = BinaryTreeNode(125)
    n150 = BinaryTreeNode(150)
    n145 = BinaryTreeNode(145, right=n150)
    n140 = BinaryTreeNode(140, right=n145)
    n130 = BinaryTreeNode(130, n125, n140)
    n110 = BinaryTreeNode(110)
    n120 = BinaryTreeNode(120, n110, n130)

    r1 = BinaryTreeNode(100, n90, n120)

    return BinaryTree(r1)


if __name__ == "__main__":
    tree = create_a_binary_tree()
    tree.in_order(tree.root)
    print(f"in-order      :    {tree.inorder}")
    tree.in_order_stack(tree.root)
    print(f"in-order stack:    {tree.inorder}")
    tree.post_order(tree.root)
    tree.pre_order(tree.root)
    print(f"pre-order      :   {tree.preorder}")
    tree.pre_order_stack(tree.root)
    print(f"pre-order stack:   {tree.preorder}")
    print(f"post-order:        {tree.postorder}")
