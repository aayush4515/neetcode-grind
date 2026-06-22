class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we are going to use a frequency map for this
        # we create frequency map for each string and then compare to see if they're equal
        # if they're equal, return True
        # else, return False

        freq_s = dict()
        freq_t = dict()

        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        return freq_s == freq_t