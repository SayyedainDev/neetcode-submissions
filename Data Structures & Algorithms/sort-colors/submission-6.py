class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        R = len(nums) - 1
        i = 0
        
        while i <= R:
            if nums[i] == 0:
                nums[L], nums[i] = nums[i], nums[L]
                L += 1
                i += 1  
            elif nums[i] == 1:
                i += 1
            else:
                nums[R], nums[i] = nums[i], nums[R]
                R -= 1