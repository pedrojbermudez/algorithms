'''
  URL:
    https://leetcode.com/problems/coin-change/

  Explanation:
    You are given an integer array coins representing coins of different 
    denominations and an integer amount representing a total amount of money.

    Return the fewest number of coins that you need to make up that amount. If 
    that amount of money cannot be made up by any combination of the coins, 
    return -1.

    You may assume that you have an infinite number of each kind of coin.

  Constraints:
    * 1 <= coins.length <= 12
    * 1 <= coins[i] <= (2^31) - 1
    * 0 <= amount <= 10^4

  Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

  Example 2:
    Input: coins = [2], amount = 3
    Output: -1

  Example 3:
    Input: coins = [1], amount = 0
    Output: 0
'''

from typing import List

class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    if (
      amount < 0
      or amount > 10**4
      or len(coins) < 1 
      or len(coins) > 12
    ):
      return -1

    coins.sort(reverse=True)
    total_coins = 0

    while amount != 0:
      loop_breaked = False

      for coin in coins:
        if amount - coin >= 0:
          amount -= coin
          total_coins += 1
          loop_breaked = True

          break
      
      if not loop_breaked:
        return -1
    
    return total_coins

def main():
  sol = Solution()
  
  print(sol.coinChange(coins = [1,2,5], amount = 11))
  print(sol.coinChange(coins = [2], amount = 3))
  print(sol.coinChange(coins = [1], amount = 0))
  print(sol.coinChange(coins = [2,3,4,5,9,48], amount = 10**4))
  print(sol.coinChange(coins = [2], amount = 3))
  print(sol.coinChange(coins = [1], amount = 0))

if __name__ == '__main__':
  main()