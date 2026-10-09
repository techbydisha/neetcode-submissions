class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
        # time Compl: O(n) worst case as nums inc, the if would also increase rounds
        # space Compl: O(n) set would increase if nums increase and no duplicate is detected.