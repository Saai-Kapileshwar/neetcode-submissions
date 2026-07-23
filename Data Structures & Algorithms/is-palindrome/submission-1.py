class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = [c.lower() for c in s if c.isalnum()]
        return p == p[::-1]