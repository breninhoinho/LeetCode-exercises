class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            word = '-' + str(x)[-1:0:-1]
        else: 
            word = str(x)[::-1]
        result = int(word)
        if result > (2**31)-1 or result < -(2**31):
            return 0
        else:
            return result

resp = Solution()
print(resp.reverse(1534236469))