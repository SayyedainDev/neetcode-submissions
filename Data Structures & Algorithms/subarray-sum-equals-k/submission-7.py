class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1}
        res=0
        prefix=0

        for i in range(len(nums)):
            prefix+=nums[i]
            diff=prefix-k
            res+=freq.get(diff,0)
            freq[prefix]=freq.get(prefix,0)+1
        return res


