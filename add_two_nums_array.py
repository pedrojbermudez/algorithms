'''
  URL:
    https://leetcode.com/problems/add-two-numbers/

  Exaplanation:
    You are given two non-empty linked lists representing two 
    non-negative integers. The digits are stored in reverse order, 
    and each of their nodes contains a single digit. Add the two 
    numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

  Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

  Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807

  Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

  Example 3:
    Input: 
      l1 = [9,9,9,9,9,9,9]
      l2 = [9,9,9,9]
    Output: [8, 9, 9, 9, 0, 0, 0, 1]
'''

def add_two_nums(l1, l2):
  lenL1 = len(l1)
  lenL2 = len(l2)

  if lenL2 > lenL1:
    l1, l2 = l2, l1
    lenL1, lenL2 = lenL2, lenL1

  counter = 0
  output = []

  for i in range(lenL1):
    value1 = l1[i]
    value2 = 0

    if i < lenL2:
      value2 = l2[i]
    
    total = int(value1 + value2 + counter)

    if total > 9:
      counter = int(total / 10)
      output.append(total % 10)
    else:
      counter = 0
      output.append(total)

  if counter > 0:
    output.append(counter)

  return output

def main():
  print(add_two_nums([2,4,3], [5,6,4]))


if __name__ == '__main__':
  main()