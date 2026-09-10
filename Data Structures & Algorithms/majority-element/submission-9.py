class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        majority=len(nums)//2
        for num in freq:
            if freq[num]>=majority:
                return num
        return -1
        