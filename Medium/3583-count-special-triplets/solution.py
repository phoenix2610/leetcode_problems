from collections import Counter
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        right_count = Counter(nums)
        left_count = Counter()
        triplets = 0
        
        for mid_val in nums:
            right_count[mid_val] -= 1
            target = mid_val * 2
            
            triplets += left_count[target] * right_count[target]

            left_count[mid_val] += 1

        return triplets   