class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        res = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[left])
                left += 1
            res = max(res, r - left + 1)
            seen.add(s[r])
        return res