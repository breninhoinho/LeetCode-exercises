class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_size = 1
        for i in range(len(s)-1):
            list_word = []
            size = 0 
            j = i
            while j<=len(s)-1 and  s[j] not in ''.join(list_word):
                list_word.append(str(s[j]))
                size +=1
                j +=1
            if size > max_size:
                max_size = size

        return max_size
    
resp = Solution()
print(resp.lengthOfLongestSubstring(''))


# s ='pwwkew'
# for i in range(0,len(s)-1):
#     list_word = []
#     size = 0 
#     j = i
#     while j<=len(s)-1 and s[j] not in ''.join(list_word):
#         list_word.append(str(s[j]))
#         size +=1
#         j +=1
#         print(list_word,j)