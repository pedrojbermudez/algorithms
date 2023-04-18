'''
  URL:
    https://leetcode.com/problems/reverse-integer/

  Explanation:
    Given a signed 32-bit integer x, return x with its digits reversed. If 
    reversing x causes the value to go outside the signed 32-bit integer range 
    [-2^31, 2^31 - 1], then return 0.
    
    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

  Constraints:

  Example 1:
    Input: x = 123
    Output: 321

  Example 2:
    Input: x = -123
    Output: -321

  Example 3:
    Input: x = 120
    Output: 21
'''
import math


def reverse_integer(num: int) -> int:
  result = 0

  if num < (-2)**31 or num > (2**31)-1:
    return 0

  while num != 0:
    pop = int(math.fmod(num, 10))
    num = int(num / 10)

    result = result * 10 + pop

  return result

def main():
  print(reverse_integer(123)) # 321
  print(reverse_integer(-123)) # -321
  print(reverse_integer(120)) # 21
  print(reverse_integer(-81238123)) # -32183218
  print(reverse_integer(123456789)) # 987654321
  print(reverse_integer(987654321)) # 123456789
  print(reverse_integer(123432)) # 234321
  print(reverse_integer(542324)) # 423245
  print(reverse_integer(44444)) # 44444
  print(reverse_integer(4444324234234234244)) # 0
  print(reverse_integer(-4444324234234234244)) # 0

if __name__ == '__main__':
    main()
