class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        q=set(nums)
        long = 0
        for n in q:
            if(n-1) not in q:
                l = 1
                while (n+l) in q:
                    l+=1
                long=max(long,l)
        return long

