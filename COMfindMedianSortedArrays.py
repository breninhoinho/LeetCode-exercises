class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        for i in nums2:
            nums1.append(i)

        nums1.sort()
        n = len(nums1)

        if len(nums1) % 2 == 0:
            mid1 = nums1[n//2-1]
            mid2 = nums1[n//2]
            res = (mid1 + mid2)/ 2.0
            return res
        else:
            return nums1[n//2]
        
resp = Solution()

lista1 = [1,3,4,5]
lista2 = [2,6]

media = resp.findMedianSortedArrays(lista1,lista2)
print(media)