class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            needed=target-nums[i]
            if needed in freq:
                return [freq[needed],i]
            freq[nums[i]]=i

       