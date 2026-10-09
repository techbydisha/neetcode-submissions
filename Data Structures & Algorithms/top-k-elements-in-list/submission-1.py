# BucketSort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums: #this is our sorted dict where we see the occurance of each
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items(): #number and freq in count
            freq[c].append(n) # we have added nums list for each freq, freq is the index value
        res = []
        for i in range(len(freq) -1, 0, -1): #go over the bucket starting from last to first
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    # Space - O(n)
    # Time - O(n)
            


