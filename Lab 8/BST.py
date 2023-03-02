compare = 0


class Node:
    key = None
    value = None
    left = None
    right = None

    def __init__(self, k, v):
        self.key = k
        self.value = v

    def insert(self, k, v):
        global compare
        if self.key == k:
            compare = compare + 1
            self.v = v
            return
        elif k < self.key:
            compare = compare + 1
            # remove pass and add your code here
            # if left child is none, add the node as the left child
            # else call the left child to insert the node
            if self.left is None:
                self.left = Node(k, v)
            else:
                self.left.insert(k, v)

        else:
            compare = compare + 1
            # remove pass and add your code here
            # if right child is none, add the node as the right child
            # else call the right child to insert the node
            if self.right is None:
                self.right = Node(k, v)
            else:
                self.right.insert(k, v)


input = input("Enter a list of letters to insert into the binary tree separated by commas:\n")
input = input.split(",")

root = Node(input[0], 1)
for i in range(1, len(input)):
    root.insert(input[i], 2)

print("Number of compares to create the BST =", compare)