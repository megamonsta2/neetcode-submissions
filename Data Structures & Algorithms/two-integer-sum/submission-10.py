class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found: dict[int,int] = {}
        # Stores the difference between target and num, in found (with the index of the num), if it finds the difference anywhere else in the array, it means the current index (num2) and the index of the difference (num1) are the result
        for i in range(len(nums)):
            num = nums[i]
            if num in found:
                return[found[num], i]
            else:
                found[target - num] = i