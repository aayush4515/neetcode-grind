# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # stores the numbers in an ascending order after in-order traversal
    def __init__(self):
        self.nums = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # do an in-order dfs traversal and append the elements to a list
        # by default, it will be in ascending order

        # helper function for travseral
        def inorder(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return
            
            inorder(node.left)
            self.nums.append(node.val)
            inorder(node.right)
        
        # sort the numbers
        inorder(root)

        # find the kth smallest
        return self.nums[k - 1]



