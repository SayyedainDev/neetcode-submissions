class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        for i in range(len(first)):
            current_char = first[i]

            for word in strs[1:]:
                if i >= len(word):
                    return first[:i]

                if word[i] != current_char:
                    return first[:i]

        return first