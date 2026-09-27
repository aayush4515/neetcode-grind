# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # base cases
        
        # check if the current node is one of the given nodes
        # if yes, that node is the common ancestor of both the nodes
        if root.val == p.val or root.val == q.val:
            return root
        
        # check if p and q are in two different subtrees
        # this is where the split happens and the root of the current subtree
        # is the common ancestor of both the nodes
        if p.val < root.val and q.val > root.val or p.val > root.val and q.val < root.val:
            return root

        # recursive case, if both are either to the left or to the right of the current node
        if p.val < root.val and q.val < root.val:
            # traverse the left subtree recursively
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            # traverse the right subtree recursively
            return self.lowestCommonAncestor(root.right, p, q)
