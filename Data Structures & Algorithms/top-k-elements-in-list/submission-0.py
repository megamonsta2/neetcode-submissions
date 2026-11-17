class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        found: dict[int, int] = {}
        for n in nums:
            if n in found:
                found[n] += 1
            else:
                found[n] = 1

        sortedFound = sorted(list(found.keys()), key=lambda x: found[x], reverse=True)

        # minAmt = 10^4
        # mostImportant = []
        # for n in found:
        #     amt = found[n]
        #     if len(mostImportant) < k:
        #         for i in range(len(mostImportant)):
        #             if (found[mostImportant[i]] < amt)
        #             mostImportant.insert()
        #         mostImportant[n] = amt
        #         minAmt = min(minAmt, amt)
        #         continue

        #     if amt > minAmt:

        result = []
        for i in range(k):
            result.append(sortedFound[i])
        return result
