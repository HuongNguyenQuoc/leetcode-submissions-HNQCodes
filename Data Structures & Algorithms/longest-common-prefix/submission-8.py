class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        for i in range(len(first_word)):
            c = first_word[i]
            for next_word in strs[1:]:
                if i >= len(next_word) or c != next_word[i]:
                    return first_word[:i]        
        return first_word