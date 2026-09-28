# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    pos_inf = float('inf')
    neg_inf = float('-inf')

    left_bound = neg_inf
    right_bound = pos_inf

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node: Optional[TreeNode], left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not node:
                return True
            
            # base case
            if not(node.val > left and node.val < right):
                return False
            
            # recursive case
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, self.left_bound, self.right_bound)

                


        




