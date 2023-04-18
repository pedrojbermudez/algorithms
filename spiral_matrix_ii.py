'''
  URL:
    https://leetcode.com/problems/spiral-matrix-ii/

  Explanation:
    Given a positive integer n, generate an n x n matrix filled with elements
    from 1 to n2 in spiral order.

  Example 1:
    Input: n = 3
    Output: [[1,2,3],[8,9,4],[7,6,5]]
  
  Example 2:
    Input: n = 1
    Output: [[1]]

    Constraints:
      - 1 <= n <= 20
'''


from time import time

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
      if n < 1 or n > 20:
        return
      current_num = 1
      row = 0
      col = 0
      col_dir = 1
      row_dir = 0
      number_list = [[0 for _ in range(n)] for _ in range(n)]
      total_inside_loop = 0

      while current_num <= n**2:
        number_list[row][col] = current_num
        current_num += 1
        
        if col == n - 1 - total_inside_loop and row == 0 + total_inside_loop:
          # Going down
          col_dir = 0
          row_dir = 1
        elif col == n - 1 - total_inside_loop and row == n - 1 - total_inside_loop:
          # Going left
          col_dir = -1
          row_dir = 0
        elif col == 0 + total_inside_loop and row == n - 1 - total_inside_loop:
          # Going up
          col_dir = 0
          row_dir = -1
          total_inside_loop += 1
        elif col == -1 + total_inside_loop and row == 0 + total_inside_loop:
          # Going right
          col_dir = 1
          row_dir = 0

        col += col_dir
        row += row_dir

      return number_list

def main():
  start = time()
  sol = Solution()
  print("1 => ", sol.generateMatrix(1), end='\n\n')
  print("2 => ", sol.generateMatrix(2), end='\n\n')
  print("3 => ", sol.generateMatrix(3), end='\n\n')
  print("4 => ", sol.generateMatrix(4), end='\n\n')
  print("5 => ", sol.generateMatrix(5), end='\n\n')
  print("6 => ", sol.generateMatrix(6), end='\n\n')
  print("7 => ", sol.generateMatrix(7), end='\n\n')
  print("8 => ", sol.generateMatrix(8), end='\n\n')
  print("9 => ", sol.generateMatrix(9), end='\n\n')
  print("10 => ", sol.generateMatrix(10), end='\n\n')
  print("11 => ", sol.generateMatrix(11), end='\n\n')
  print("12 => ", sol.generateMatrix(12), end='\n\n')
  print("13 => ", sol.generateMatrix(13), end='\n\n')
  print("14 => ", sol.generateMatrix(14), end='\n\n')
  print("15 => ", sol.generateMatrix(15), end='\n\n')
  print("16 => ", sol.generateMatrix(16), end='\n\n')
  print("17 => ", sol.generateMatrix(17), end='\n\n')
  print("18 => ", sol.generateMatrix(18), end='\n\n')
  print("19 => ", sol.generateMatrix(19), end='\n\n')
  print("20 => ", sol.generateMatrix(20), end='\n\n')
  print("21 => ", sol.generateMatrix(21), end='\n\n')
  end = time()

  print(end-start)

if __name__ == '__main__':
  main()