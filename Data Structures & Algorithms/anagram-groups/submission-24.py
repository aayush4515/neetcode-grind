from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ord_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            ord_dict[tuple(count)].append(s)

        # build the resulting list from values of the ord_dict
        return list(ord_dict.values())

