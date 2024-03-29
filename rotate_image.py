'''
  URL:
    https://leetcode.com/problems/rotate-image/

  Explanation:
    You are given an n x n 2D matrix representing an image, rotate the image by 
    90 degrees (clockwise).

    You have to rotate the image in-place, which means you have to modify the 
    input 2D matrix directly. DO NOT allocate another 2D matrix and do the 
    rotation.

  Constraints:
    - n == matrix.length == matrix[i].length
    - 1 <= n <= 20
    - -1000 <= matrix[i][j] <= 1000
  Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

  Example 2:
    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''

class Solution:
  def checkMatrix(self, matrix):
    len_m = len(matrix)

    for i in range(len_m):
      if len_m != len(matrix[i]):
        return False
      
      for j in range(len_m):
        if matrix[i][j] > 1000 or matrix[i][j] < -1000:
          return False
    return True
  
  def rotate(self, matrix):
    if self.checkMatrix(matrix):
      matrix.reverse()
      for i in range(len(matrix)):
        for j in range(i):
          matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def main():
  matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
  matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
  sol = Solution()
  sol.rotate(matrix1)
  sol.rotate(matrix2)
  print(matrix1)
  print(matrix2)


if __name__ == '__main__':
    main()
