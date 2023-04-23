'''
    URL:
        https://leetcode.com/problems/maximum-gap/

    Explanation:
        Given an integer array nums, return the maximum difference between two 
        successive elements in its sorted form. If the array contains less than 
        two elements, return 0.

        You must write an algorithm that runs in linear time and uses linear 
        extra space.
    
    Constraints:
        - 1 <= nums.length <= 10^5
        - 0 <= nums[i] <= 10^9
    
    Example 1:
        Input: nums = [3,6,9,1]
        Output: 3
        Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or 
                     (6,9) has the maximum difference 3.
    
    Example 2:
        Input: nums = [10]
        Output: 0
        Explanation: The array contains less than 2 elements, therefore return 
                     0.
'''

def maximum_gap(nums):
    if len(nums) < 2 or len(nums) > 10**5:
        return 0

    maximum_gap = 0
    nums.sort()

    if nums[len(nums)-1] > 10**9:
        return 0

    for i in range(len(nums)-1):
        maximum_gap = max(nums[i+1] - nums[i], maximum_gap)

    return maximum_gap


def main():
    print(maximum_gap([3, 6, 9, 1]))
    print(maximum_gap([3, 60, 90, 1]))
    print(maximum_gap([10]))


if __name__ == '__main__':
    main()
