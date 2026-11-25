class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        queue = deque()
        gridcpy = deepcopy(grid)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append([r,c])
                elif grid[r][c]==1:
                    fresh+=1
        minutes = 0
        while len(queue)!=0 and fresh>0:
            minutes+=1
            rotten = len(queue)
            for _ in range(rotten):
                i,j = queue.popleft()
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_i, new_j = dx+i, dy+j
                    if new_i <0 or new_i>= rows or new_j <0 or new_j >= cols or grid[new_i][new_j]!=1:
                        continue
                    fresh -=1
                    grid[new_i][new_j]=2
                    queue.append([new_i,new_j])
        if fresh>0:
            return -1
        return minutes