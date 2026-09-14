class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        zeros = [num for num in nums if num == 0]
        non_zero = [num for num in nums if num != 0] 
        nums[:] = non_zero + zeros
