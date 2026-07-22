class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        q = {}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in q:
                return [q[diff], i]
            q[n]=i
