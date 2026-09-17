from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       freq={}
       for i in range(len(strs)):
            s=''.join(sorted(strs[i]))
            if s not in freq:
                freq[s]=[]
            freq[s].append(strs[i])
       return list(freq.values())

           
        


        