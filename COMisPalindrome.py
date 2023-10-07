class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

resp = Solution()
print(resp.isPalindrome(2234))       