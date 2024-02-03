from typing import List


def majorityElement(nums: List[int]) -> int:
    m, c = 0, 0
    for ele in nums:
        if c == 0:
            m = ele
        if ele == m:
            c += 1
        else:
            c -= 1
    return m
    
print(majorityElement([3,3,4]))

print(majorityElement([3,2,3]))

print(majorityElement([2,2,1,1,1,2,2]))
