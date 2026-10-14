class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in range(len(nums)):
            count[nums[i]]=count.get(nums[i],0)+1
        
        buckets=[[] for i in range(len(nums)+1)]

        for item , count in count.items():
            buckets[count].append(item)
        res=[]
        for i in range(len(buckets)-1,0,-1):
            for s in buckets[i]:
                res.append(s)
            if len(res)==k:
                return res


