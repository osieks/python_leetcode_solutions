from typing import List

def merge( nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    i=m-1
    j=n-1
    k=m+n-1
    
    for x in range(m,m+n):
        try:
            nums1[x]=0
        except:
            nums1.append(0)
    
    while i>=0:
        if j>=0 and nums1[i]<nums2[j]:
            nums1[k]=nums2[j]
            j-=1
        else:
            nums1[k]=nums1[i]
            i-=1
        k-=1
              
    print(nums1)

nums1 =[1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1,m,nums2,n)

nums1 = [1]
m = 1
nums2 = []
n = 0

merge(nums1,m,nums2,n)

nums1 = [0]
m = 0
nums2 = [1]
n = 1

merge(nums1,m,nums2,n)