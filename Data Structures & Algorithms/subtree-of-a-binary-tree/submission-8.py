# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # initial BFS + recursive DFS
        # use initial BFS to find the nodes in Root tree that is the root of Subroot tree, and add those nodes to candidate_nodes
        # if such a node does not exist, return False
        # if they do exist, perform recursive DFS from those node (treat as root) and the Subroot tree
        # match the structure and value of both trees, return True if matching
        # return False if not matching

        # note: visited set not required for binary trees

        # edge cases
        if not root:
            return False
        if not subRoot:
            return True
        if not root and not subRoot:
            return True


        # initial BFS, match roots
        candidate_nodes = []
        queue = deque([root])
        startNode = None

        while queue:
            node = queue.popleft()
            if node:

                if node.val == subRoot.val:
                    startNode = node
                    candidate_nodes.append(node)
                
                queue.append(node.left)
                queue.append(node.right)
        
        if not startNode:
            return False
        

        # recursive DFS using startNode and subRoot to check if tree is same
        # use a helper
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        # go through all candidate nodes and compare each with the subRoot, return True if any match, else return False
        for node in candidate_nodes:
            if isSameTree(node, subRoot):
                return True
        return False











