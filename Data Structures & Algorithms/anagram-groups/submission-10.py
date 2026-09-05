from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Create an array of 26 zeros
            count = [0] * 26
            
            # Count frequency of each character
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Use the tuple of counts as the dictionary key (lists are unhashable)
            anagram_map[tuple(count)].append(s)
            
        return list(anagram_map.values())