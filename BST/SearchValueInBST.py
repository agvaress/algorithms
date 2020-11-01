# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space

def searchValuetinBST(root, key):
    if root is None or root.value is key:
        return root
    if root.value < key:
        return searchValuetinBST(root.right, key)
    else:
        return searchValuetinBST(root.left, key)
