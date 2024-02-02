from typing import List
from math import floor

def removeElement(nums: List[int], val: int) -> int:
    n=0
    i=0
    while i < len(nums)-n:
        #print(nums)
        #print(nums[i])
        if nums[i]==val:
            #print("wywal")
            n+=1
            for j in range(i,len(nums)-1-n):
                nums[j]=nums[j+1]
            i-=1
        i+=1
    #print(nums)
    return nums[0:len(nums)-1-n]
   
   
nums = [1,2,3,4,5,6]
val = 3
print(removeElement(nums,val))

nums = [3,2,2,3]
val = 3
print(removeElement(nums,val))
 
nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums,val))
