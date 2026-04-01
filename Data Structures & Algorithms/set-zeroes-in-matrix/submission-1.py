class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        
        #Tìm các vị trí bằng 0 trong ma trận và đánh dấu hàng đầu tiên và cột đầu tiên tại vị trí tương ứng
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
                        
        #Convert các giá trị tại vị trí tương ứng nơi mà cột, hàng đầu tiên có giá trị = 0
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        #Xét trường hợp nếu topleft most có giá trị = 0 thì phải cho cột đầu tiên về hết = 0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        #Tương tự cho first row values = 0
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0