# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = sorted(nums1+nums2)
        size = len(res)
        mid=size//2
        if(size%2==0):
            return ((res[mid]+res[(mid)-1])/2)
        else:
            return(res[mid])
