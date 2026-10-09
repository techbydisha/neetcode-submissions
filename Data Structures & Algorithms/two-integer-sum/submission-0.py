class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {} # value: index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in numsDict:
                return [numsDict[diff], i]
            numsDict[n] = i
        return

    # have a dict with index and number
    # complement = target - num
    # if pair is there then thats the output, if it deos not then add current num to the dict with index
    # space O(n)
    # time(O(n))
