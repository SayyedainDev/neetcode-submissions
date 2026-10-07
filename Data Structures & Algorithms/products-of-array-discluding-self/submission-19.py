class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product=1
        result=[]
        for i in range(len(nums)):
            result.append(prefix_product)
            prefix_product*=nums[i]
        
        postfix_product=1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=postfix_product
            postfix_product*=nums[i]
        return result
            
        