from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       freq={}
       for i in range(len(strs)):
            key=''.join(sorted(strs[i]))
            if key not in freq:
                freq[key]=[]
            freq[key].append(strs[i])
       return list(freq.values())



      
        


        