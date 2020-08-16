
## squares of a sorted array
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        print(A)
        A = list(map(lambda x:x**2,A))
        return sorted(A)

## replace elements with greatest element on the right side
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)==1:
            return [-1]
        arr[0]=max(arr[1:])
        for i in range(1,len(arr)-1):
            if arr[i] != arr[i-1]:
                arr[i]=arr[i-1]
            else:
                val=max(arr[i+1:])
                arr[i]=val
        arr[-1]=-1
        return arr

## Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_ = 1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[len_] = nums[i]
                len_ +=1
        return len_
    
    


## move zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(i)
        return nums
