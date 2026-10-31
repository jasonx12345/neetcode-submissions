from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: if the grid is empty, there are 0 islands
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])  # Fixed: get columns from the first row length
        visited = set()
        islands = 0
        
        # BFS algorithm to explore the entire connected island
        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c)) # Mark starting node as visited

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    next_r, next_c = row + dr, col + dc
                    
                    # Check bounds, if it's land ("1"), and if it hasn't been visited yet
                    if (next_r in range(rows) and 
                        next_c in range(cols) and 
                        grid[next_r][next_c] == "1" and 
                        (next_r, next_c) not in visited):
                        
                        q.append((next_r, next_c))
                        visited.add((next_r, next_c)) # Mark as visited immediately when adding to queue

        # Go through every single cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find land ("1") that hasn't been visited, it's a new island!
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
                    
        return islands