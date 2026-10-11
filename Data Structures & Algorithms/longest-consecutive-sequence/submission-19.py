class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        def mergesort(arr,l,m,r):
            left=arr[l:m+1]
            right=arr[m+1:r+1]
            i=l
            j=0
            k=0
            while j<len(left) and k<len(right):
                if left[j]<right[k]:
                    arr[i]=left[j]
                    j+=1
                else:
                    arr[i]=right[k]
                    k+=1
                i+=1
            while j <len(left):
                arr[i]=left[j]
                j+=1
                i+=1
            while k <len(right):
                arr[i]=right[k]
                k+=1
                i+=1



        def merge(arr,l,r):

            if l>=r:
                return arr

            m=(l+r)//2

            merge(arr,l,m)
            merge(arr,m+1,r)
            mergesort(arr,l,m,r)


        merge(nums,0,len(nums)-1)
        count=1 
        longest=1
        if not nums:
            return 0
        #1,2,3,4,200,300
        for i in range(1,len(nums)):
            
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                count+=1
            else:
                count=1
            longest=max(count,longest)
        return longest




        