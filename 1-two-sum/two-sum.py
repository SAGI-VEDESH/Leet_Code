class Solution:
    # Time: O(n)
    # Space: O(n)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # value -> index
        for i, cur in enumerate(nums):
            # cur + x = target
            # x = target - cur
            x = target - cur
            if x in seen:
                return [seen[x], i]
            seen[cur] = i

        return None