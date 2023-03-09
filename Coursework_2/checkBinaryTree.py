""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    # Use the inorder traversal to check if the tree is a binary search tree
    sequence = inorder_trav(root)
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False
    return True


def inorder_trav(root):
    if root is None:
        return []
    return inorder_trav(root.left) + [root.data] + inorder_trav(root.right)