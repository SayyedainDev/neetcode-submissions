from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            
            # If we encounter duplicates at l, mid, and r, we can't tell which side is sorted
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            # Left half is strictly sorted
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1   
            # Right half is strictly sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Note: Your original code had r = mid - 1 here, which was incorrect
                else:
                    r = mid - 1
                    
        return False
