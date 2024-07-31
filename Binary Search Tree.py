class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left:
                self._insert(data, node.left)
            else:
                node.left = TreeNode(data)
        else:
            if node.right:
                self._insert(data, node.right)
            else:
                node.right = TreeNode(data)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data)
            self._inorder(node.right)

# Example usage
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.inorder()  # Output: 3 5 7
