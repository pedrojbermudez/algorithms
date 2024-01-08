"""
https://leetcode.com/problems/add-two-numbers-ii/
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class FastestSolution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []

        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        total_sum = 0
        carry = 0
        output = ListNode()
        while s1 or s2:
            if s1:
                total_sum += s1.pop()
            if s2:
                total_sum += s2.pop()

            output.val = total_sum % 10
            carry = total_sum // 10
            head = ListNode(carry)
            head.next = output
            output = head
            total_sum = carry

        return output.next if carry == 0 else output

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        current = output
        carry = 0

        def get_next(l: Optional[ListNode]):
            if l:
                yield from get_next(l.next)
                yield l.val
       
        val1 = []
        for val in get_next(l1):
            val1.append(val)

        val2 = []
        for val in get_next(l2):
            val2.append(val)

        i = 0
        j = 0
        carry = 0
        a = [0] * (max(len(val1), len(val2)) + 1)
        k = -1

        while i < len(val1) or j < len(val2):
            sum = carry
           
            if i < len(val1):
                sum += val1[i]

            if j < len(val2):
                sum += val2[j]

            carry = sum // 10

            sum = sum % 10
            a[k] = sum

            i += 1
            j += 1
            k -= 1
        if carry != 0:
            a[0] = carry

        if (len(a) > 1 and a[0] == 0):
            a = a[1:]
        for num in a:
            current.next = ListNode(num)
            current = current.next
        return output.next


l1 = ListNode(5)
l2 = ListNode(5)

from time import time
sool = Solution()
sool2 = FastestSolution()

start_time = time()
for _ in range(100_000_000):
    a = sool.addTwoNumbers(l1, l2)
end_time = time()
print(end_time - start_time)

start_time = time()
for _ in range(100_000_000):
    a = sool2.addTwoNumbers(l1, l2)
end_time = time()
print(end_time - start_time)
while a:
    print(a.val)
    a = a.next