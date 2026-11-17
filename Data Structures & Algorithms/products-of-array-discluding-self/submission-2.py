class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        amt = len(nums)
        result = [1] * amt
        for n in nums:
            total *= n
        for i in range(amt):
            n = nums[i]
            if n == 0:
                currentTotal = 1
                for j in range(amt):
                    if i == j:
                        continue
                    currentTotal *= nums[j]
                result[i] = currentTotal
            else:
                result[i] = int(total / n)
        return result

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        amt = len(nums)
        result = [1] * amt
        for i in range(amt):
            for j in range(amt):
                if i == j:
                    continue
                result[j] *= nums[i]
        return result
