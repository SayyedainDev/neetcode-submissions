class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        candidate=None
        for i in range(len(nums)):
            if nums[i]==candidate:
                count+=1
            elif count==0:
                candidate=nums[i]
            else:
                count-=1
        return candidate