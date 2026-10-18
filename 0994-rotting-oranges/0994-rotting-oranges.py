class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        grid_cpy = deepcopy(grid)
        fresh = 0
        queue = deque()
        
        #for getting number of rotten locations
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        minutes = 0

        #now neeed to see then nearby to rooten 
        while fresh>0 and len(queue)!=0:
            minutes +=1
            total = len(queue)
            for _ in range(total):
                i,j=queue.popleft()
                #now i had the rotten values now need to check left, right, up , down of it 
                for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_i,new_j = i+x,j+y
                    #write edge cases 
                    if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                        continue
                    if grid_cpy[new_i][new_j]==2 or grid_cpy[new_i][new_j]==0:
                        continue
                    grid_cpy[new_i][new_j]=2
                    fresh-=1
                    queue.append((new_i,new_j))
        return minutes if fresh == 0 else -1 # if fresh == 0 then returns the min else  -1 
