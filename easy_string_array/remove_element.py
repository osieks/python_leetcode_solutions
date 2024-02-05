from typing import List
from math import floor

def removeElement(nums: List[int], val: int) -> int:
    n = 0
    for i in range(0,len(nums)):
        if nums[i] != val:
            nums[n]=nums[i]
            n+=1
    return nums[0:n]
   
   
nums = [1,2,3,4,5,6]
val = 3
print(removeElement(nums,val))

nums = [3,2,2,3]
val = 3
print(removeElement(nums,val))
 
nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums,val))
