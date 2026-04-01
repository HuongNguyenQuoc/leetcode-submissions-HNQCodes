class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            row = mid // n # Tìm vị trí của hàng vì mỗi hàng chứa n phần tử, ví dụ mỗi hàng có 4 phần tử thì biết mid / 4 sẽ ra vị trí hàng
            col = mid % n #Phép chia dư tìm vị trí cột trong hàng
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        '''
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        def binary_search(l: int, r: int) -> bool:
            if l > r:
                return False
            mid = (l + r) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                return binary_search(mid + 1, r)
            else:
                return binary_search(l, mid - 1)
        return binary_search(l, r)
            
