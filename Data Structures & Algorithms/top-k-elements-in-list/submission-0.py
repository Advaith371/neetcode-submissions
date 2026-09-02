class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans_with_count = Counter(nums).most_common(k)
        ans = []
        for i in ans_with_count:
            ans.append(i[0])
        return ans