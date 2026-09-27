# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # simple BFS
        level = 1
        queue = deque([(root, level)])
        res_dict = defaultdict(list)

        while queue:
            curr, level = queue.popleft()

            if curr:
                res_dict[level].append(curr.val)

                level += 1
                queue.append((curr.left, level))
                queue.append((curr.right, level))

        # return the values of res_dict as a list
        return list(res_dict.values())
