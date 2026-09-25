class Solution:
    def recursive_search(self,nums: list[int],target: int, start: int, end: int) -> int:
        if start > end:
            return -1

        mid = start + (end - start) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.recursive_search(nums, target, start, mid - 1)
        else:
            return self.recursive_search(nums, target, mid + 1, end)

    def search(self, nums: list[int], target: int) -> int:
        return self.recursive_search(nums, target, 0,len(nums) - 1)