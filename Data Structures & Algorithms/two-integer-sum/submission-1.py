class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return [0,0]


        # two numbers sum up to target, it cannot be the same number.
        # have i and j (i+1)
        # iterate and Add and find the target
        # Time O(n^2)
        # Space: O(1), not O(n). You never create a structure that grows with the input.
            