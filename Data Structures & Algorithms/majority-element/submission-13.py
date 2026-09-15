class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        candidate=None
        for i in range(len(nums)):
            if count==0:
                candidate=nums[i]
                count+=1
            elif candidate==nums[i]:
                count+=1
            else:
                count-=1
        return candidate