from typing import List


class Solution:
   
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the array to the right by k positions.
        Modify nums in-place.
        """

        n = len(nums)
        k = k % n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # Step 1: Reverse the whole array
        reverse(0, n - 1)

        # Step 2: Reverse the first k elements
        reverse(0, k - 1)

        # Step 3: Reverse the remaining elements
        reverse(k, n - 1)