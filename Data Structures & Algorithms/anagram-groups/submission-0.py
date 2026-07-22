class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = {}
        for s in strs:
            count = tuple(sorted(s))
            if count in r:
                r[count].append(s)
            else:
                r[count] = [s]
        return list(r.values())