from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num_islands = 0
        directions = [
            (1, 0),    # down
            (-1, 0),   # up
            (0, 1),    # right
            (0, -1),   # left
        ]

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                q = deque()
                if grid[m][n] == '1' and (m,n) not in visited:
                    print("num_islands: ", num_islands)
                    print("(m,n):", (m,n))
                    
                    q.append((m,n))
                    visited.add((m,n))
                    while q:
                        # print("visited: ", visited)
                        print("queue: ", q)
                        curr_r, curr_c = q.popleft()
                        print("curr_r, curr_c: ", curr_r, curr_c)
                        for dr, dc in directions:
                            nr = dr + curr_r
                            nc = dc + curr_c
                            print("nr, nc: ", nr, nc)
                            if (
                                0 <= nr < len(grid)
                                and 0 <= nc < len(grid[0])
                                and (nr, nc) not in visited
                            ):
                                print("jhere")
                                visited.add((nr, nc))
                                print(f"grid[{nr}][{nc}] = {grid[nr][nc]}")
                                if grid[nr][nc] == '1':
                                    print("this is a 1")
                                    q.append((nr, nc))
                        
                    num_islands += 1
        print("num_islands: ", num_islands)

        return num_islands