class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for i in nums:
            if i not in table:
                table[i] = 0
            table[i] += 1
        sorted_dict = dict(sorted(table.items(), key=lambda item: -item[1]))
        ans = []
        srt = [i for i in sorted_dict]
        for i in range(k):
            ans.append(srt[i])
        return ans
            