class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       frequency={}
       for num in nums:
          if num in frequency:
             return num
          frequency[num]=1
            

            