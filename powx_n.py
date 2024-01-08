"""
    URL:
        https://leetcode.com/problems/powx-n/description/

    Problem:
        Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

    Constraints:
        - -100.0 < x < 100.0
        - -2^31 <= n <= 2^31-1
        - n is an integer.
        - Either x is not zero or n > 0.
        - -10^4 <= x^n <= 10^4

    Example 1:
        Input: x = 2.00000, n = 10
        Output: 1024.00000

    Example 2:
        Input: x = 2.10000, n = 3
        Output: 9.26100

    Example 3:
        Input: x = 2.00000, n = -2
        Output: 0.25000
        Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n < 0:
            flag = -1
        else:
            flag = 1
        
        n = abs(n)
        while n != 0:
            if n % 2 == 0:
                x = x * x
                n = n // 2
            else:
                ans = ans * x
                n = n-1

        if flag == -1:
            return 1 / ans

        return ans

def main():
    sol = Solution()
    print(sol.myPow(0.00001, 2147483647))


if __name__ == '__main__':
    main()
