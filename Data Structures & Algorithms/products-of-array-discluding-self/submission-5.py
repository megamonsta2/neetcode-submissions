class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        total = 1
        for n in nums:
            if n == 0:
                zeros += 1
                continue
            total *= n

        if zeros > 1:
            return [0] * len(nums)
        elif zeros == 1:
            return [total if n == 0 else 0 for n in nums]
        else:
            return [int(total / n) for n in nums]

