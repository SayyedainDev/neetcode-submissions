class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)
        i=0
        while low < high:
            medium=(low+high)//2
            number=nums[medium]

            if number > target:
                high=medium
            elif number<target:
                low=medium+1
            elif number==target:
                return medium
            
        return -1
            
        