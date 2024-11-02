from typing import List


# Merge Sort Solution
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(arr):
            if len(arr) == 1:
                return arr

            arrayOne = arr[: len(arr) // 2]
            arrayTwo = arr[len(arr) // 2 :]

            arrayOne = mergeSort(arrayOne)
            arrayTwo = mergeSort(arrayTwo)

            return merge(arrayOne, arrayTwo)

        def merge(arr1, arr2):
            array = []

            while len(arr1) > 0 and len(arr2) > 0:
                if arr1[0] > arr2[0]:
                    array.append(arr2[0])
                    arr2.remove(arr2[0])
                else:
                    array.append(arr1[0])
                    arr1.remove(arr1[0])
            while arr1:
                array.append(arr1[0])
                arr1.remove(arr1[0])
            while arr2:
                array.append(arr2[0])
                arr2.remove(arr2[0])

            return array

        return mergeSort(nums)
