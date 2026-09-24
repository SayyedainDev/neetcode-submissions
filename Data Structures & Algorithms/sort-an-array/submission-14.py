from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        def merge(arr, L, M, R):
            left = arr[L:M+1]
            right = arr[M+1:R+1]
            i, j, k = L, 0, 0

            # Compare elements from left and right temporary arrays
            while j < len(left) and k < len(right):
                if right[k] < left[j]:
                    arr[i] = right[k]
                    k += 1
                else:
                    arr[i] = left[j]
                    j += 1
                i += 1

            # Copy remaining elements
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergesort(arr, l, r):
            if l >= r:
                return arr

            mid = (l + r) // 2
            mergesort(arr, l, mid)
            mergesort(arr, mid + 1, r)
            merge(arr, l, mid, r)
            
            return arr

        return mergesort(nums, 0, len(nums) - 1)