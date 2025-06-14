# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            if s[end] in char_map and char_map[s[end]] >= start:
                start = char_map[s[end]] + 1
            char_map[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length