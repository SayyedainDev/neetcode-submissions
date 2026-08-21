class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=nums[i]
            else:
                return True
        return False
            

                
        