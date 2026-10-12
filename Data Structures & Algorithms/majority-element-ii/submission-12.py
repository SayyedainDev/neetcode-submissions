class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        result=[]
        n=len(nums)
        for item , count in freq.items():
            if count>n//3:
                result.append(item)
        return result

        