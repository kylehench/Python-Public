# In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

def solution(matrix):
    
    r_len = len(matrix)
    c_len = len(matrix[0])
    # print(r_len, c_len)
    res = [[0-matrix[r][c] for c in range(c_len)] for r in range(r_len)]
    for r in range(r_len):
        if r > 0:
            for c in range(c_len):
                print(r, c)
                res[r][c] += sum(matrix[r-1][max(0,c-1):min(c+2, c_len)])
        
        for c in range(c_len):
            res[r][c] += sum(matrix[r][max(0,c-1):min(c+2, c_len)])
            
        if r < r_len-1:
            for c in range(c_len):
                res[r][c] += sum(matrix[r+1][max(0,c-1):min(c+2, c_len)])
    return res