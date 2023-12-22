"""
    URL:
        https://leetcode.com/problems/add-two-numbers/
    
    Problem:
        You are given two non-empty linked lists representing two non-negative
        integers. The digits are stored in reverse order, and each of their 
        nodes contains a single digit. Add the two numbers and return the sum as
        a linked list.

        You may assume the two numbers do not contain any leading zero, except 
        the number 0 itself.

    Constraints:
        - The number of nodes in each linked list is in the range [1, 100].
        - 0 <= Node.val <= 9
        - It is guaranteed that the list represents a number that does not have
          leading zeros.

    Example 1:
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.

    Example 2:
        Input: l1 = [0], l2 = [0]
        Output: [0]

    Example 3:
        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]
"""
from typing import List, Optional

class ListNode:
    def __init__(self, val: int = 0, next = None):
        if not isinstance(val, int):
            raise TypeError("Value must be int type") 
        elif val < 0 or val > 9:
            raise ValueError("Value must be between 0 and 9 (both inclusive)")

        self.val = val
        self.next = next


    def __str__(self) -> str:
        output = str(self.val)
        head = self.next
        while head:
            output += "," + str(head.val)
            head = head.next
        return output


class Solution:
    def add_two_numbers(self, 
                        l1: Optional[ListNode], 
                        l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(0)
        current = output
        carry = 0
        total = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            carry = sum // 10
            
            # Avoiding leading zeroes for l1 as [0,0,0,0] and l2 = [0]
            total = total * 10 + (sum % 10)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        for digit in str(total):
            current.next = ListNode(int(digit))
            current = current.next

        return output.next


    def generate_list(self, nums: Optional[List]) -> Optional[ListNode]:
        if nums is None or len(nums) < 1 or len(nums) > 100:
            return None

        list_node = ListNode(0)
        head = list_node

        for num in nums:
            new_node = ListNode(num)
            head.next = new_node
            head = head.next

        return list_node.next


def example1(sol: Solution):
    """
        Input: 
            l1 = [2,4,3]
            l2 = [5,6,4]

        Output: 
            [7,0,8]
    """
    l1 = sol.generate_list([2,4,3])
    l2 = sol.generate_list([5,6,4])
    l3 = sol.add_two_numbers(l1=l1, l2=l2)

    print(l3)


def example2(sol: Solution):
    """
        Input: 
            l1 = [0]
            l2 = [0]

        Output: 
            [0]
    """
    l1 = sol.generate_list([0,0,0,0,0])
    l2 = sol.generate_list([0])
    l3 = sol.add_two_numbers(l1=l1, l2=l2)

    print(l3)


def example3(sol: Solution):
    """
        Input: 
            l1 = [9,9,9,9,9,9,9] 
            l2 = [9,9,9,9]

        Output: 
            [8,9,9,9,0,0,0,1]
    """
    l1 = sol.generate_list([9,9,9,9,9,9,9])
    l2 = sol.generate_list([9,9,9,9])
    l3 = sol.add_two_numbers(l1=l1, l2=l2)
    
    print(l3)


def main():
    sol = Solution() 
    example1(sol)
    example2(sol)
    example3(sol)


if __name__ == '__main__':
    main()
