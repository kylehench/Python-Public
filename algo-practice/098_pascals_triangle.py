# Given an integer numRows, return the first numRows of Pascal's triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for _ in range(numRows-1):
            triangle.append([a+b for a, b in zip([0]+triangle[-1], triangle[-1]+[0])])
        return triangle