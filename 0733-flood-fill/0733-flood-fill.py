from collections import deque
from copy import deepcopy

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image

        dup = deepcopy(image)
        rows = len(dup)
        cols = len(dup[0])
        init_color = dup[sr][sc]

        queue = deque()
        queue.append((sr, sc))
        dup[sr][sc] = color

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while queue:
            i, j = queue.popleft()

            for x, y in directions:
                new_i = i + x
                new_j = j + y

                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue

                if dup[new_i][new_j] != init_color:
                    continue

                # Mark visited BEFORE adding to the queue
                dup[new_i][new_j] = color
                queue.append((new_i, new_j))

        return dup