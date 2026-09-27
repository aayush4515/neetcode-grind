# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # comparing both trees at once
        queue = deque([(p, q)])

        while queue:
            p_node, q_node = queue.popleft()

            # both positions are none: matching structure
            if p_node == None and q_node == None:
                continue

            # one is none and the other is not: not matching
            if p_node == None or q_node == None:
                return False

            # check if value is same
            if p_node.val != q_node.val:
                return False

            # append the left and the right nodes
            queue.append((p_node.left, q_node.left))
            queue.append((p_node.right, q_node.right))
        return True

