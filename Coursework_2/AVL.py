import os
import sys


class BST:
    root = None

    def put(self, key, val):
        self.root = self.put2(self.root, key, val)

    def put2(self, node, key, val):
        if node is None:
            # key is not in tree, create node and return node to parent
            return Node(key, val)
        if key < node.key:
            # key is in left subtree
            node.left = self.put2(node.left, key, val)
        elif key > node.key:
            # key is in right subtree
            node.right = self.put2(node.right, key, val)
        else:
            node.val = val
        return node

    def createTree(self, a):

        for x in a:
            n = x.split(":")
            self.put(n[0], n[1])

    # Create a AVL Tree, you are allowed to create other helper functions
    def createBalancedTree(self, a):
        for x in a:
            n = x.split(":")
            self.insertAVL(n[0], n[1])

    # preOrder Traversal, this should be a recursive function
    def preOrder(self, node):
        if node is None:
            return []
        return [node.key + ":" + node.val] + self.preOrder(node.left) + self.preOrder(node.right)

    # inOrder Traversal, this should be a recursive function
    def inOrder(self, node):
        if node is None:
            return []
        return self.inOrder(node.left) + [node.key + ":" + node.val] + self.inOrder(node.right)

    # postOrder Traversal, this should be a recursive function
    def postOrder(self, node):
        if node is None:
            return []
        return self.postOrder(node.left) + self.postOrder(node.right) + [node.key + ":" + node.val]

    # given a key, obtain its value
    def get(self, key):
        return self.get2(self.root, key)

    # given a key, find the node and obtain the depth, you are allowed to create other helper functions
    def depth(self, key):
        return self.depth2(self.root, key, 0)

    # given a key, find the node and obtain the height, you are allowed to create other helper functions
    def height(self, key):
        return self.height2(self.root, key)

    # given a key, find the node and obtain the size, you are allowed to create other helper functions
    def size(self, key):
        return self.size2(self.root, key)

    # given a key, delete the node, you are allowed to create other helper functions
    def delete(self, key):
        self.root = self.delete2(self.root, key)
        return True

    def get2(self, root, key):
        if root is None:
            return None
        if key < root.key:
            return self.get2(root.left, key)
        elif key > root.key:
            return self.get2(root.right, key)
        else:
            return root.val

    def size2(self, root, key):
        if root is None:
            return 0
        if key < root.key:
            return self.size2(root.left, key) + 1
        elif key > root.key:
            return self.size2(root.right, key) + 1
        else:
            return self.size2(root.left, key) + self.size2(root.right, key)

    def depth2(self, root, key, param):
        if root is None:
            return 0
        if key < root.key:
            return self.depth2(root.left, key, param + 1)
        elif key > root.key:
            return self.depth2(root.right, key, param + 1)
        else:
            return param

    def height2(self, current_node, key):
        if current_node is None:
            return -1
        else:
            return max(self.height2(current_node.left, key), self.height2(current_node.right, key)) + 1

    def delete2(self, root, key):
        if root is None:
            return None
        # Search for key to delete
        if key < root.key:
            root.left = self.delete2(root.left, key)
        elif key > root.key:
            root.right = self.delete2(root.right, key)
        else:
            # Found key
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right
            # Node has two children
            temp = root
            root = self.min(temp.right)
            root.right = self.deleteMin(temp.right)
            root.left = temp.left
        return root

    def deleteMin(self, node):
        if node.left is None:
            return node.right
        node.left = self.deleteMin(node.left)
        return node

    def min(self, right):
        if right.left is None:
            return right
        return self.min(right.left)

    def getBalance(self, root):
        if not root:
            return 0
        return self.getAVLHeight(root.left) - self.getAVLHeight(root.right)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        return y

    def getAVLHeight(self, root):
        if not root:
            return -1
        return 1 + max(self.getAVLHeight(root.left), self.getAVLHeight(root.right))

    def insertAVL(self, key, val):
        self.root = self.insertAVL2(self.root, key, val)

    def insertAVL2(self, root, key, val):
        if not root:
            return Node(key, val)
        elif key < root.key:
            root.left = self.insertAVL2(root.left, key, val)
        else:
            root.right = self.insertAVL2(root.right, key, val)
        balance = self.getBalance(root)
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

class Node:
    left = None
    right = None
    key = 0
    val = 0

    def __init__(self, key, val):
        self.key = key
        self.val = val


array = input("Enter a list of key:value pairs separated by commas:\n")
array = [str(x) for x in array.split(",")]

bst = BST()
bst.createTree(array)

###testcase 0 (get())
for i in range(2):
    key1 = input("Input key for get() method:\n")
    if key1 != '-':
        print("The value of", key1, "is", bst.get(key1))

###testcase 1 (size(),depth(),height())
key1 = input("Input key for size() method:\n")
if key1 != '-':
    print("The size of", key1, "is", bst.size(key1))

key1 = input("Input key for depth() method:\n")
if key1 != '-':
    print("The depth of", key1, "is", bst.depth(key1))

key1 = input("Input key for height() method:\n")
if key1 != '-':
    print("The height of", key1, "is", bst.height(key1))

print()

###testcase 2 (preOrder(), inOrder(), postOrder())
print("The preOrder traversal is", bst.preOrder(bst.root))
print("The inOrder traversal is", bst.inOrder(bst.root))
print("The postOrder traversal is", bst.postOrder(bst.root))
print()

###testcase 3 delete()
for i in range(2):
    key1 = input("Input key for delete() method:\n")
    if key1 != '-':
        print("Deleting", key1, "is", bst.delete(key1))
        print("The preOrder traversal is", bst.preOrder(bst.root))
        print("The inOrder traversal is", bst.inOrder(bst.root))
        print("The postOrder traversal is", bst.postOrder(bst.root))

###testcase 4 createbalancedTree()
key1 = input("Test balanced Tree? \n")
if key1 == 'Y':
    bst = BST()
    bst.createBalancedTree(array)
    print("The preOrder traversal is", bst.preOrder(bst.root))
    print("The inOrder traversal is", bst.inOrder(bst.root))
    print("The postOrder traversal is", bst.postOrder(bst.root))
