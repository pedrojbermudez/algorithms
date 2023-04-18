from random import randint
from time import time

class QuickSort:
  def __partition(self, arr, low, high, i, j):
    mid = low
    pivot = arr[high]

    while mid <= high :
      if arr[mid] < pivot:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1
      elif arr[mid] == pivot:
        mid += 1
      elif arr[mid] > pivot:
        arr[high], arr[mid] = arr[mid], arr[high]
        high -= 1

    i = low - 1
    j = mid # or high + 1

    return i, j

  def sort(self, array, low, high):
    if low < high:
      i = low
      j = high
      i, j = self.__partition(array, low, high, i, j)
      self.sort(array, low, i)
      self.sort(array, j, high)

class MergeSortTwoArrays:
  def qsort(self, arr):
    qsort = QuickSort()
    qsort.sort(arr, 0, len(arr) - 1)
  
  def sortedMerge(self, arr1, arr2):
    # res = arr1 + arr2
    res = []

    for i in range(len(arr1)):
      res.append(arr1[i])
    
    for i in range(len(arr2)):
      res.append(arr2[i])
      
    self.qsort(res)

    return res
def main():
  a = [randint(0, 25) for _ in range(10)]
  b = [randint(0, 25) for _ in range(11)]

  start_time = time()
  res = (MergeSortTwoArrays()).sortedMerge(a, b)
  end_time = time()

  print(end_time - start_time)
  print(res)

if __name__ == '__main__':
  main()