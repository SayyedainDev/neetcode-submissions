from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the array to the right by k positions.
        Modify nums in-place.
        """

        n = len(nums)

        # In case k is greater than the length of the array
        k = k % n

        def reverse(left,right):
            while left<right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
            
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)