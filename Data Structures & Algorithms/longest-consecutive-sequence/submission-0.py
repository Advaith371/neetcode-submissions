class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        hashset = set()
        for num in nums:
            hashset.add(num)

        result = 0
        for num in hashset:
            if num - 1 not in hashset:
                next = num
                while next in hashset:
                    next += 1
                result = max(result, next - num)
        
        return result