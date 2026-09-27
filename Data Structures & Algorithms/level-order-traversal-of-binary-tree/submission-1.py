# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # without using a dictionary

        queue = deque([root])
        result = []
        
        while queue:
            level_res = []
            len_q = len(queue)

            for i in range(len_q):
                curr = queue.popleft()
                if curr:
                    level_res.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
                
            if level_res:
                result.append(level_res)
        
        return result