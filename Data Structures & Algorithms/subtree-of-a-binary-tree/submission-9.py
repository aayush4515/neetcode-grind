# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # similar BFS + DFS solution as Solution 1 but instead of having a list of candidate nodes, we check the nodes in-place inside BFS

        # define the helper DFS function
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        # start BFS on the root tree
        if not root:
            return False
        if not subRoot:
            return True
        if not root and not subRoot:
            return True

        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                # check if node equals subRoot
                if node.val == subRoot.val:
                    # this is a candidate node, now check if both trees are same
                    if isSameTree(node, subRoot):
                        return True
                    
                queue.append(node.left)
                queue.append(node.right)
            
        # if no match, return False
        return False