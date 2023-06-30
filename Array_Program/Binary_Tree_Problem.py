# Binary Tree Problem

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def inorder_traversal(root):
    if root is None:
        return

    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)


# Example usage
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Perform inorder traversal
print("Inorder Traversal:")
inorder_traversal(root)
