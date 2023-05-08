'''
  URL:
    https://leetcode.com/problems/median-of-two-sorted-arrays/

  Exaplanation:
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return
    the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).

  Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -10^6 <= nums1[i], nums2[i] <= 10^6

  Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

  Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''

class Solution:
  def findMedianSortedArrays(self, nums1, nums2):
    nums3 = nums1 + nums2
    nums3.sort()

    if len(nums3) % 2 == 1:
      return nums3[len(nums3) // 2]
    else:
      median = len(nums3) // 2
      return (float(nums3[median]) + float(nums3[median-1])) / 2

def main():
  sol = Solution()
  print(sol.findMedianSortedArrays([1], [2]))
  print(sol.findMedianSortedArrays([1,3], [2]))
  print(sol.findMedianSortedArrays([1,2], [3,4]))
  print(sol.findMedianSortedArrays([1,2,3,4,5], [6,7,8,9,10]))

if __name__ == '__main__':
  main()