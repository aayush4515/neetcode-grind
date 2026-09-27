# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        visited_p = []
        visited_q = []

        queue_p = deque([p])
        queue_q = deque([q])

        # p tree
        while queue_p:
            node = queue_p.popleft()

            if not node:
                visited_p.append(None)
                continue

            visited_p.append(node.val)
            queue_p.append(node.left)
            queue_p.append(node.right)
        
        # q tree
        while queue_q:
            node = queue_q.popleft()

            if not node:
                visited_q.append(None)
                continue

            visited_q.append(node.val)
            queue_q.append(node.left)
            queue_q.append(node.right)

        return visited_p == visited_q
