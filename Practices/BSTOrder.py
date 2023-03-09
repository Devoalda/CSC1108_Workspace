# Class describing a node of tree
class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v

    def insert(self, v):
        if self.data:
            if v < self.data:
                if self.left is None:
                    self.left = Node(v)
                else:
                    self.left.insert(v)
            elif v > self.data:
                if self.right is None:
                    self.right = Node(v)
                else:
                    self.right.insert(v)
        else:
            self.data = v

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(chr(self.data), end=" ")
        if self.right:
            self.right.printTree()

# Inorder Traversal
def printInorder(root):
    if root:
        # Traverse left subtree
        printInorder(root.left)

        # Visit node
        print(chr(root.data), end=" ")

        # Traverse right subtree
        printInorder(root.right)


# Preorder Traversal
def printPostOrder(node):
    if node is None:
        return

    # Traverse left subtree
    printPostOrder(node.left)

    # Traverse right subtree
    printPostOrder(node.right)

    # Visit Node
    print(chr(node.data), end=" ")


# Preorder Traversal
def printPreOrder(node):
    if node is None:
        return
    # Visit Node
    print(chr(node.data), end=" ")

    # Traverse left subtree
    printPreOrder(node.left)

    # Traverse right subtree
    printPreOrder(node.right)


# Driver code
if __name__ == "__main__":
    # Build the tree
    root = Node(ord('E'))
    #root.left = Node(ord('A'))
    #root.right = Node(ord('S'))
    #root.right.right = Node(ord('Y'))
    #root.right.right.left = Node(ord('U'))
    #root.right.right.left.left = Node(ord('S'))
    #root.right.right.left.left.right = Node(ord('T'))
    #root.right.left = Node(ord('Q'))
    #root.right.left.left = Node(ord('E'))
    #root.right.left.left.right = Node(ord('I'))
    #root.right.left.left.right.right = Node(ord('O'))
    #root.right.left.left.right.right.left = Node(ord('N'))

    # Insert EASYQUESTION
    root.insert(ord('A'))
    root.insert(ord('S'))
    root.insert(ord('Y'))
    root.insert(ord('Q'))
    root.insert(ord('U'))
    root.insert(ord('E'))
    root.insert(ord('I'))
    root.insert(ord('O'))
    root.insert(ord('N'))

    # Print the tree
    print("Tree:")
    root.printTree()


    # Function call
    print("Inorder Traversal:", end=" ")
    printInorder(root)
    print("\nPreorder Traversal:", end=" ")
    printPreOrder(root)
    print("\nPostorder Traversal:", end=" ")
    printPostOrder(root)

# This code is contributed by ajaymakvana.
