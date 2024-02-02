from typing import List
from math import floor

def remove_duplicates(nums: List[int]) -> int:
    """
    in non-decreasing order, remove the duplicates
    """
    j = 0
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
    return j + 1
   
   
nums = [1,1,2]
print(remove_duplicates(nums))

nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(nums))