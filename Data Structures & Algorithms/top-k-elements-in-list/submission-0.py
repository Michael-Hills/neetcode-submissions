class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for i in nums:
            frequency[i] += 1

        ordered = sorted(frequency.items(), key=lambda pair: pair[1],reverse=True)
        return [num for num, _ in ordered[:k]]