import collections
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: if the tree is empty, return an empty list
        if not root:
            return []
            
        # List to store the final result grouped by levels
        result = []
        
        # Initialize a queue for Breadth-First Search (BFS) and start with the root node
        q = collections.deque()
        q.append(root)

        # Loop as long as there are nodes to explore in the queue
        while q:
            # Capture the exact number of nodes at the *current* level right now
            q_len = len(q)
            level = []
            
            # Process every node belonging strictly to this current level
            for i in range(q_len):
                node = q.popleft()   # Remove the node from the front of the queue
                level.append(node.val) # Add its value to our current level list
                
                # If a left child exists, push it to the queue for the next level
                if node.left:
                    q.append(node.left)
                    
                # If a right child exists, push it to the queue for the next level
                if node.right:
                    q.append(node.right)
            
            # Once the level is fully gathered, add it to our final result list
            result.append(level)
            
        return result