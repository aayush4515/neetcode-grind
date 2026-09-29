# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # similar to Solution 1 but using a hashmap instead of calling inorder.index() because it is an O(N) lookup

        io_indices = dict()         # io: inorder
        io_indices = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        # helper function to build the tree
        def help_build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            if left > right:
                return None
            
            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)

            mid = io_indices[root_val]
            root.left = help_build(left, mid - 1)
            root.right = help_build(mid + 1, right)
            return root
        
        # build the tree now
        result = help_build(0, len(inorder) - 1)

        return result
