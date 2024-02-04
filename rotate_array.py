from typing import List


def rotate(nums: List[int], k: int) -> None:
    tmp = nums[len(nums)-k:]
    print(tmp)
    for i in range(1,len(nums)-k+1):
        nums[len(nums)-i]=nums[len(nums)-i-k]
    nums[0:k]=tmp
    print(nums)
     
print(rotate([1,2,3,4,5,6,7],3))
print(rotate([-1,-100,3,99],2))

def rotate2(nums: List[int], k: int) -> None:
    tmp = nums[]
    print(tmp)
    
    
print(rotate2([1,2,3,4,5,6,7],3))
print(rotate2([1,2],3))
print(rotate2([-1,-100,3,99],2))