class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        left = 0
        right = n * n - 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def canReach(row, column, max_time, visited):

            if row == n - 1 and column == n - 1:
                return True
            
            visited.add((row, column))

            for dr, dc in directions:
                nr, nc = row + dr, column + dc

                if (0 <= nr < n and 0 <= nc < n and
                 (nr, nc) not in visited and
                 grid[nr][nc] <= max_time):
                    if canReach(nr, nc, max_time, visited):
                        return True

            return False


        while left <= right:
            mid = (left + right) // 2
            visited = ()

            if canReach(0, 0, mid, visited):
                best_time = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best_time