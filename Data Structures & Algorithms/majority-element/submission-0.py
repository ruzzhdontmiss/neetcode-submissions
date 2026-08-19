



class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        count_map = {}

        for num in nums:
            if num not in count_map:
                count_map[num] = 0

            count_map[num] += 1

            if count_map[num] > n / 2:
                return num