class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        majority=len(nums)//2
        for i in range(len(freq)):
            if freq[nums[i]]>=majority:
                return nums[i]
        return -1
        