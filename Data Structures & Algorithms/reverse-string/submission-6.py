class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        S = 0
        e = len(s) - 1  # 1. Correct the ending index
        
        while S < e:    # 2. Change the loop condition
            # 3. Use Pythonic swapping to fix the overriding issue
            s[S], s[e] = s[e], s[S] 
            
            S += 1
            e -= 1