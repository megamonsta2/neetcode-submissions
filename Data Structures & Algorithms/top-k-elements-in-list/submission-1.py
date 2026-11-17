class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        found: dict[int, int] = {}
        for n in nums:
            if n in found:
                found[n] += 1
            else:
                found[n] = 1

        sortedFound = sorted(list(found.keys()), key=lambda x: found[x], reverse=True)

        result = []
        for i in range(k):
            result.append(sortedFound[i])
        return result
