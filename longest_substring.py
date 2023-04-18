'''
  URL:
    https://leetcode.com/problems/longest-substring-without-repeating-characters/

  Exaplanation:
    Given a string s, find the length of the longest substring without repeating
    characters.

  Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

  Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

  Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

  Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
from time import time
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    output = ""
    max_length = 0

    for c in s:
      if c not in output:
        output += c
      else:
        if max_length < len(output):
          max_length = len(output)
        output = c
    
    if max_length < len(output):
      return len(output)

    return max_length

def main():
  sol = Solution()
  start_time = time()
  for _ in range(1_000_000):
    sol.lengthOfLongestSubstring("abcabcbb")
    sol.lengthOfLongestSubstring("bbbbb")
    sol.lengthOfLongestSubstring("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
  end_time = time()
  
  print(end_time - start_time)

if __name__ == '__main__':
  main()