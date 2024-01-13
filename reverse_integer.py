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
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        min_value = -2 ** 31
        max_value = 2 ** 31 - 1

        while x != 0:
            if result < min_value / 10 or result > max_value / 10:
                return 0

            digit = x % 10 if x > 0 else x % -10
            result = result * 10 + digit
            x = int(x / 10)

        return result

def main():
    sol = Solution()
    print(sol.reverse(-10)) # -1
    print(sol.reverse(1534236469)) # 0
    print(sol.reverse(123)) # 321
    print(sol.reverse(-123)) # -321
    print(sol.reverse(120)) # 21
    print(sol.reverse(-81238123)) # -32183218
    print(sol.reverse(123456789)) # 987654321
    print(sol.reverse(987654321)) # 123456789
    print(sol.reverse(123432)) # 234321
    print(sol.reverse(542324)) # 423245
    print(sol.reverse(44444)) # 44444
    print(sol.reverse(4444324234234234244)) # 0
    print(sol.reverse(-4444324234234234244)) # 0

if __name__ == '__main__':
    main()
