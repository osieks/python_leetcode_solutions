from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]+nums[y]==target:
                    return [x,y]
        return [0,0]
    

nums = [1,2,3,4,5,6]
print(twoSum(nums,7)) #twoSum