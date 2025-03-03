# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Given two integer arrays preorder and inorder where preorder is the preorder traversal
# of a binary tree and inorder is the inorder traversal of the same tree, construct and
# return the binary tree.

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]


# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def values(self):
        left = [None] if not self.left else self.left.values()
        right = [None] if not self.right else self.right.values()
        return [self.val, *left, *right]


def construct_binary_tree(preorder: list[int], inorder: list[int]):
    if inorder:
        root = preorder.pop(0)

        root_inorder_index = inorder.index(root)

        root = TreeNode(root)
        root.left = construct_binary_tree(preorder, inorder[:root_inorder_index])
        root.right = construct_binary_tree(preorder, inorder[root_inorder_index + 1 :])

        return root


def traverse_preorder(node: TreeNode) -> list[int]:
    values = []
    if node:
        values.append(node.val)
        values.extend(traverse_preorder(node.left))
        values.extend(traverse_preorder(node.right))
    return values


# Test Cases:
# Case 1:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
expected_result = [3, 9, 20, 15, 7]

tree = construct_binary_tree(preorder, inorder)
result = traverse_preorder(tree)

assert result == expected_result, result
